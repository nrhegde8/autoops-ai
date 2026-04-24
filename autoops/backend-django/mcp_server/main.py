from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "MCP Server Running"}


# 🔥 ADD THIS
class CityRequest(BaseModel):
    city: str


@app.post("/select-courier")
def select_courier(req: CityRequest):
    
    city = req.city.lower()

    if city == "delhi":
        courier = "DTDC"
    elif city == "mumbai":
        courier = "BlueDart"
    elif city == "bangalore":
        courier = "Ekart"
    else:
        courier = "Delhivery"

    return {"recommended_courier": courier}