import requests

def create_order(product_name: str, weight: str, city: str):

    try:
        response = requests.post(
            "http://127.0.0.1:8000/api/orders/create/",
            json={
                "product_name": product_name,
                "weight": weight,
                "city": city
            }
        )

        if response.status_code == 200 or response.status_code == 201:
            return {
                "status": "success",
                "message": f"Order created for {product_name} to {city}"
            }

        else:
            return {
                "status": "error",
                "message": "Failed to create order in backend"
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }