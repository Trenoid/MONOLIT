import logging
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import context
from projects.models import Categories, Projects
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

from main.forms import ContactForm, BigContactForm
from main.models import FAQ
from main.models import Contact_informations
from users.models import EmailVerification
from django.views.decorators.csrf import csrf_exempt
from .tasks import send_email_task

logger = logging.getLogger(__name__)

# class IndexView(TemplateView):
#     template_name = "main/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         faqs = FAQ.objects.all()
#         context['title'] = 'Monolith'
#         context['faqs'] = faqs
#         context['form'] = ContactForm()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Обработка данных формы (например, отправка email)
#             # name = form.cleaned_data['name']
#             # phone_number = form.cleaned_data['phone_number']
#             # city = form.cleaned_data['city']
#             return JsonResponse({'status': 'success'})
#         return JsonResponse({'status': 'error', 'errors': form.errors})

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faqs = FAQ.objects.all()
        context['title'] = 'Monolith'
        context['faqs'] = faqs
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']
            message = ""

            if request.user.is_authenticated:
                try:
                    created_account = EmailVerification.objects.get(user=request.user).created
                    status_email = request.user.is_verified_email
                    message = (
                        f"Monolith.\n\nЗарегистрированным пользователем заполнена форма для обратной связи.\n\n"
                        f"Заявка со следующими данными:\nИмя: {name}\nНомер телефона: {phone_number}\nГород: {city}\n"
                        f"Статус верификации почты: {status_email}\nПочта: {request.user.email}"
                    )
                except EmailVerification.DoesNotExist:
                    logger.error(f"EmailVerification record not found for user {request.user}")
            else:
                message = (
                    f"Monolith.\n\nНе зарегистрированным пользователем заполнена форма для обратной связи\n\n"
                    f"Заявка со следующими данными:\nИмя: {name}\nНомер телефона: {phone_number}\nГород: {city}\n"
                )

            logger.info(f"Sending email with message: {message}")
            recipient_list = [Contact_informations.objects.first().mail_for_from]

            try:
                send_email_task.delay(
                    "Новая заявка на сайте Monolith",
                    message,
                    recipient_list,
                )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                return JsonResponse({'status': 'error', 'errors': str(e)})
        else:
            logger.error(f"Form errors: {form.errors}")
        return JsonResponse({'status': 'error', 'errors': form.errors})


def index(request):

    faqs = FAQ.objects.all()

    context = {
        'title' : 'Monolith',
        'faqs' : faqs
    }

    return render(request,'main/index.html',context)


def about(request):
    form = ContactForm()
    context = {
        'title' : 'О компании',
    }
        
    return render(request,"main/about-company.html",context)

# def services(request):
#     context = {
#         'title' : 'Услуги',
#         'form' : ContactForm(),
#     }
        
#     return render(request, "main/services.html",context)

def services(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']

            # Формирование и отправка письма
            subject = "Новая заявка с сайта"
            message = f"Имя: {name}\nНомер телефона: {phone_number}\nГород: {city}"
            recipient_list = [settings.EMAIL_HOST_USER]  # ваш email адрес

            send_email_task.delay(
                subject,
                message,
                recipient_list,
            )

            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ContactForm()

    context = {
        'title': 'Услуги',
        'form': form,
    }

    return render(request, "main/services.html", context)

# def quiz(request):
#     if request.method == 'POST':
#         form = BigContactForm(request.POST)
#         if form.is_valid():
#             print("form is valid")

#             # Получение email получателя
#             recipient_email = Contact_informations.objects.first().mail_for_from
#             if not recipient_email:
#                 print("Recipient email is not set")
#                 return redirect('main:index')

#             recipient_list = [recipient_email]

#             # Получение данных формы
#             cleaned_data = form.cleaned_data
#             house_area = cleaned_data['house_area']
#             floors = cleaned_data['floors']
#             materials = ', '.join(cleaned_data['materials'])
#             house_height = cleaned_data['house_height']
#             facades = ', '.join(cleaned_data['facades'])
#             foundation = ', '.join(cleaned_data['foundation'])
#             garage = ', '.join(cleaned_data['garage'])
#             bath = ', '.join(cleaned_data['bath'])
#             terrace = ', '.join(cleaned_data['terrace'])
#             pool = ', '.join(cleaned_data['pool'])
#             land_area = cleaned_data['land_area']
#             name = cleaned_data['name']
#             phone_number = cleaned_data['phone_number']
#             email = cleaned_data['email']

#             # Формирование сообщения email
#             subject = 'Итоги квиза'
#             message = f"""
#             Имя: {name}
#             Номер телефона: {phone_number}
#             Email: {email}
            
#             Площадь дома: {house_area}
#             Этажи: {floors}
#             Материалы: {materials}
#             Высота дома: {house_height} м
#             Отделка фасадов: {facades}
#             Фундамент: {foundation}
#             Гараж: {garage}
#             Баня: {bath}
#             Терасса: {terrace}
#             Бассейн: {pool}
#             Площадь земельного участка: {land_area} соток
#             """

#             print(message)

#             # Отправка email
#             try:
#                 send_mail(
#                     subject,
#                     message,
#                     settings.EMAIL_HOST_USER,
#                     recipient_list,
#                     fail_silently=False,
#                 )
#                 print("Email sent successfully")
#             except Exception as e:
#                 print(f"Error sending email: {e}")

#             # Перенаправление на страницу успеха
#             return redirect('main:index')
#         else:
#             print("Form is not valid")
#             print(form.errors)
#     else:
#         form = BigContactForm()
    
#     context = {
#         'title': "Квиз",
#         'form': form,
#     }
#     return render(request, "main/quiz.html", context)


@csrf_exempt
def quiz(request):
    if request.method == 'POST':
        form = BigContactForm(request.POST)
        if form.is_valid():
            recipient_email = Contact_informations.objects.first().mail_for_from
            if not recipient_email:
                print("{'status': 'error', 'message': 'Recipient email is not set'}")
                return JsonResponse({'status': 'error', 'message': 'Recipient email is not set'})

            recipient_list = [recipient_email]

            cleaned_data = form.cleaned_data
            house_area = cleaned_data['house_area']
            floors = cleaned_data['floors']
            materials = ', '.join(cleaned_data['materials'])
            house_height = cleaned_data['house_height']
            facades = ', '.join(cleaned_data['facades'])
            foundation = ', '.join(cleaned_data['foundation'])
            garage = ', '.join(cleaned_data['garage'])
            bath = ', '.join(cleaned_data['bath'])
            terrace = ', '.join(cleaned_data['terrace'])
            pool = ', '.join(cleaned_data['pool'])
            land_area = cleaned_data['land_area']
            name = cleaned_data['name']
            phone_number = cleaned_data['phone_number']
            email = cleaned_data['email']

            subject = 'Итоги квиза'
            message = f"""
            Заполнен квиз со следующими данными для сайта Monolith
            Имя: {name}
            Номер телефона: {phone_number}
            Email: {email}
            
            Площадь дома: {house_area}
            Этажи: {floors}
            Материалы: {materials}
            Высота дома: {house_height} м
            Отделка фасадов: {facades}
            Фундамент: {foundation}
            Гараж: {garage}
            Баня: {bath}
            Терасса: {terrace}
            Бассейн: {pool}
            Площадь земельного участка: {land_area} соток
            """
            
            try:
                send_email_task.delay(
            subject,
            message,
            recipient_list,
        )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'status': 'error', 'message': str(e)})

        return JsonResponse({'status': 'error', 'errors': form.errors})
    
    else:
        form = BigContactForm()
    
    context = {
        'title': "Квиз",
        'form': form,
    }
    return render(request, "main/quiz.html", context)