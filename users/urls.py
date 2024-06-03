from django.urls import path

from users.views import login, account, registration , logout,recovery_account,users_cart

app_name = "users"

urlpatterns = [
    path('login/', login, name='login'),
    path('account/', account, name='account'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('users-cart/', users_cart, name='users_cart'),
    path('recovery_account/', recovery_account, name='recovery_account'),

]
