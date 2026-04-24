import requests

def create_order(product_name: str, weight: str, city: str):

    # 🔥 DEBUG: check if tool is getting called
    print("🔥 TOOL CALLED:", product_name, weight, city)

    try:
        res = requests.post(
            "http://127.0.0.1:8000/api/orders/create/",
            json={
                "product_name": product_name,
                "weight": weight,
                "city": city
            }
        )

        # 🔥 DEBUG: check Django response
        print("📦 DJANGO RESPONSE:", res.status_code, res.text)

        return {
            "status": "success",
            "message": f"Order created for {product_name} to {city}",
            "data": res.json()
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }


      