from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, account, registration , logout,recovery_account,users_cart,email_ver,pay
from users.views import LoginView, RegistrationView, AccountView, EmailVerificationView,OrderCreateView

app_name = "users"


# class view
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('account/', login_required(AccountView.as_view()), name='account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
    path('users-cart/', users_cart, name='users_cart'),
    path('recovery_account/', recovery_account, name='recovery_account'),
    path('email_ver/<str:email>/<uuid:code>/',EmailVerificationView.as_view(),name = "email_ver"),
    path('users-cart/pay/',OrderCreateView.as_view(),name = "pay")
]


# def view
# urlpatterns = [
#     path('login/', login, name='login'),
#     path('account/', account, name='account'),
#     path('registration/', registration, name='registration'),
#     path('logout/', logout, name='logout'),
#     path('users-cart/', users_cart, name='users_cart'),
#     path('recovery_account/', recovery_account, name='recovery_account'),
#     path('email_ver/',email_ver,name = "email_ver"),

# ]