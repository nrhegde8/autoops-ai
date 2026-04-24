def select_courier_logic(city: str):
    city = city.lower()

    if city in ["chennai", "bangalore"]:
        return "Delhivery"

    elif city in ["mumbai", "delhi"]:
        return "BlueDart"

    else:
        return "DTDC"