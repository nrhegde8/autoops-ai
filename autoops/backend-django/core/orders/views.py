import json
import requests
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order


# ✅ LIST ORDERS
def list_orders(request):
    orders = list(Order.objects.values())
    return JsonResponse(orders, safe=False)


# ✅ CREATE ORDER (NO AUTH, CLEAN)
@csrf_exempt
def create_order(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"})

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"})

    product = data.get("product_name")
    weight = data.get("weight")
    city = data.get("city")

    if not product or not weight or not city:
        return JsonResponse({"error": "Missing fields"})

    # AUTO GENERATE
    order_id = str(uuid.uuid4())[:8]
    customer_name = "Guest"

    # OPTIONAL COURIER API
    try:
        courier_response = requests.post(
            "http://127.0.0.1:8002/select-courier",
            json={"city": city},
            timeout=2
        )
        courier = courier_response.json().get("recommended_courier", "default")
    except:
        courier = "default"

    order = Order.objects.create(
        order_id=order_id,
        customer_name=customer_name,
        product_name=product,
        weight=weight,
        city=city,
        courier=courier
    )

    return JsonResponse({
        "success": True,
        "data": {
            "order_id": order.order_id,
            "product_name": order.product_name,
            "weight": order.weight,
            "city": order.city,
            "courier": order.courier
        }
    })