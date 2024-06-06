
from django.urls import path

from main.views import index, about, services,quiz
from main.views import IndexView

app_name = "main"

#def views
# urlpatterns = [
#     path('', index, name='index'),
#     path('about/', about, name='about'),
#     path('services/', services, name='services'),
# ]


#class views
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('quiz/',quiz, name='quiz')
]


