from django.shortcuts import redirect, render

from carts.models import Cart
from carts.templatetags.carts_tag import user_carts
from carts.utils import get_user_carts
from projects.models import Projects



def cart_add(request, project_slug):
    project = Projects.objects.get(slug=project_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user,project=project)

        if not carts.exists():
            Cart.objects.create(user=request.user,project=project)
            
        # else:
        #     if cart:
        #         cart.save()
    else:
        carts = Cart.objects.filter(session_key = request.session.session_key ,project=project)

        if not carts.exists():
            Cart.objects.create(session_key = request.session.session_key ,project=project)

    #user_cart = get_user_carts(request)
    return redirect(request.META['HTTP_REFERER'])

    


def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id = cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])


def cart(request):

    context = {
        'title' : 'Корзина'
    }
    return render(request, "carts/cart.html", context)


