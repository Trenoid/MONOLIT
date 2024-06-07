from users.models import Order

def orders(request):
    user = request.user
    return {'orders' : Order.objects.filter(user=user) }