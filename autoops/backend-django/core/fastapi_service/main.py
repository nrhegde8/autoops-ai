from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# OPTIONAL: if you separated logic into executor.py
try:
    from executor import select_courier_logic
except:
    # fallback if executor not present
    def select_courier_logic(city: str):
        city = city.lower()

        if city in ["chennai", "bangalore"]:
            return "Delhivery"
        elif city in ["mumbai", "delhi"]:
            return "BlueDart"
        else:
            return "DTDC"


app = FastAPI()

# ✅ Allow Django to call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------- REQUEST MODEL -----------

class CityRequest(BaseModel):
    city: str


# ----------- HEALTH CHECK -----------

@app.get("/")
def home():
    return {"message": "Decision Engine Running 🚀"}


# ----------- MAIN LOGIC -----------

@app.post("/select-courier")
def select_courier(req: CityRequest):
    try:
        courier = select_courier_logic(req.city)

        return {
            "recommended_courier": courier
        }

    except Exception as e:
        return {
            "error": str(e)
        }