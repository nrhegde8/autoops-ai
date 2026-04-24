import requests
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


# ================= EMAIL FUNCTION =================
def send_email_tool(to, subject, body):
    try:
        print("📩 SENDING EMAIL...")
        print("TO:", to)

        if not EMAIL_USER or not EMAIL_PASS:
            return {
                "success": False,
                "message": "Email config missing in .env"
            }

        msg = MIMEText(body)
        msg["Subject"] = subject

        # 👇 Hide your real email (important)
        msg["From"] = "AutoOps Bot"
        msg["To"] = to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, to, msg.as_string())

        print("✅ EMAIL SENT SUCCESS")

        return {
            "success": True,
            "message": f"Email sent successfully to {to}"
        }

    except Exception as e:
        print("❌ EMAIL ERROR:", str(e))
        return {
            "success": False,
            "message": str(e)
        }


# ================= MAIN EXECUTOR =================
def execute_tool(tool_name, args):
    try:

        # ================= CREATE ORDER =================
        if tool_name == "create_order":

            print("🚀 Calling Django API...")
            print("ARGS:", args)

            res = requests.post(
                "http://127.0.0.1:8000/api/orders/create/",
                json={
                    "product_name": args.get("product_name"),
                    "weight": args.get("weight"),
                    "city": args.get("city")
                },
                timeout=5
            )

            print("STATUS:", res.status_code)
            print("RAW RESPONSE:", res.text)

            try:
                data = res.json()
            except:
                return {"error": "Invalid JSON from Django"}

            if "error" in data:
                return {
                    "success": False,
                    "message": data["error"]
                }

            return data

        # ================= SEND EMAIL =================
        elif tool_name == "send_email":

            print("🔥 EMAIL TOOL TRIGGERED")
            print("ARGS:", args)

            return send_email_tool(
                to=args.get("to"),
                subject=args.get("subject"),
                body=args.get("body")
            )

        # ================= UNKNOWN =================
        return {"error": "Unknown tool"}

    except Exception as e:
        print("❌ EXECUTOR ERROR:", str(e))
        return {"error": str(e)}