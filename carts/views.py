from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse

from carts.models import Cart
from carts.templatetags.carts_tag import user_carts
from carts.utils import get_user_carts
from projects.models import Projects




class CartAddView(View):
    def post(self, request, project_slug):
        project = Projects.objects.get(slug=project_slug)
        
        # Определение ключа пользователя или сессии
        user = request.user if request.user.is_authenticated else None
        session_key = request.session.session_key if not request.user.is_authenticated else None
        
        # Обеспечение наличия session_key для неаутентифицированных пользователей
        if not user and not session_key:
            request.session.create()
            session_key = request.session.session_key

        # Использование get_or_create для уменьшения количества запросов
        cart, created = Cart.objects.get_or_create(
            user=user,
            session_key=session_key,
            project=project,
        )

        # Если корзина была только что создана, added будет True
        response_data = {'added': created}
        return JsonResponse(response_data)
    

class CartRemoveView(View):
    def post(self, request, cart_id):
        cart = Cart.objects.get(id=cart_id)
        cart.delete()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'deleted': True})

        return redirect(request.META['HTTP_REFERER'])
    

    
# class CartAddView(View):
#     def post(self, request, project_slug):
#         project = Projects.objects.get(slug=project_slug)

#         if request.user.is_authenticated:
#             carts = Cart.objects.filter(user=request.user, project=project)

#             if not carts.exists():
#                 Cart.objects.create(user=request.user, project=project)
#         else:
#             if not request.session.session_key:
#                 request.session.create()
#             carts = Cart.objects.filter(session_key=request.session.session_key, project=project)

#             if not carts.exists():
#                 Cart.objects.create(session_key=request.session.session_key, project=project)

#         return redirect(request.META['HTTP_REFERER'])




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


