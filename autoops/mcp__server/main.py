import os
import json
import re
from dotenv import load_dotenv

print("🚀 MCP SERVER FILE LOADED")  # ✅ CONFIRM FILE LOAD

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AzureOpenAI

from executor import execute_tool
from schemas.tool_schemas import TOOLS_SCHEMA


# 🔑 ENV
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

print("🔑 ENV CHECK:")
print("API KEY:", "✅" if OPENAI_API_KEY else "❌")
print("ENDPOINT:", AZURE_ENDPOINT)
print("DEPLOYMENT:", DEPLOYMENT_NAME)


# ✅ APP
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Azure Client
client = AzureOpenAI(
    api_key=OPENAI_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT,
)


# -------- REQUEST MODEL --------
class ChatRequest(BaseModel):
    message: str


# -------- HELPERS --------
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else None


def extract_subject(text):
    match = re.search(r"subject (.*?)( body|$)", text, re.IGNORECASE)
    return match.group(1) if match else "AutoOps Email"


def extract_body(text):
    match = re.search(r"body (.*)", text, re.IGNORECASE)
    return match.group(1) if match else text


# -------- ROUTES --------

@app.get("/")
def home():
    print("🏠 HOME ROUTE HIT")
    return {"message": "MCP Server Running ✅"}


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        print("\n==============================")
        print("📩 CHAT ROUTE HIT")
        print("📩 USER MESSAGE:", req.message)

        user_text = req.message.lower()

        # ================= 🚀 EMAIL DIRECT TRIGGER =================
        if "email" in user_text or "send" in user_text:
            print("⚡ EMAIL DETECTED → DIRECT EXECUTION")

            to_email = extract_email(req.message)
            subject = extract_subject(req.message)
            body = extract_body(req.message)

            print("📧 EXTRACTED:")
            print("TO:", to_email)
            print("SUBJECT:", subject)
            print("BODY:", body)

            if not to_email:
                print("❌ NO EMAIL FOUND")
                return {"response": "❌ Please provide a valid email address"}

            result = execute_tool("send_email", {
                "to": to_email,
                "subject": subject,
                "body": body
            })

            print("✅ EMAIL RESULT:", result)

            return {
                "tool_used": "send_email",
                "result": result
            }

        # ================= 🤖 GPT CALL =================
        print("🤖 USING GPT (NO EMAIL DETECTED)")

        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are an automation assistant."},
                {"role": "user", "content": req.message}
            ],
            tools=TOOLS_SCHEMA,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        print("🤖 GPT RESPONSE:", msg)

        if msg.tool_calls:
            tool_call = msg.tool_calls[0]
            tool_name = tool_call.function.name

            args = json.loads(tool_call.function.arguments)

            print("🔥 TOOL:", tool_name)
            print("🔥 ARGS:", args)

            result = execute_tool(tool_name, args)

            print("✅ TOOL RESULT:", result)

            return {
                "tool_used": tool_name,
                "result": result
            }

        print("⚠️ NO TOOL USED")

        return {"response": msg.content}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": str(e)}