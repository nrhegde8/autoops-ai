
from django.urls import path
from .views import list_orders, create_order

urlpatterns = [
    path("", list_orders),          # → /api/orders/
    path("create/", create_order),  # → /api/orders/create/
]