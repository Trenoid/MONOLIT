from django.urls import path

from carts.views import cart_add,cart_change, cart_remove, cart

app_name = "carts"

urlpatterns = [
    path('cart_add/<slug:project_slug>/', cart_add, name='cart_add'),
    path('cart_change/<slug:project_slug>/', cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
