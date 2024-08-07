from urllib import request
from django.utils.http import urlencode
from django import template
from django.core.cache import cache

from main.models import Contact_informations


register = template.Library()

# @register.inclusion_tag('main/contact_info.html')
# def get_contact_info():
#     contact_info = Contact_informations.objects.first()
#     return {'contact_info': contact_info}


# @register.simple_tag()
# def get_contact_info():
#     contact_info = Contact_informations.objects.first()
#     contact_info_vk = contact_info.vk 
#     return {'contact_info' : contact_info, 'contact_info_vk' : contact_info_vk}


@register.simple_tag()
def get_contact_info_vk():
    return Contact_informations.objects.first().vk

@register.simple_tag()
def get_contact_info_inst():
    return Contact_informations.objects.first().instagramm

# @register.simple_tag()
# def get_contact_info_number():
#     return Contact_informations.objects.first().number

@register.simple_tag()
def get_contact_info_number():
    return Contact_informations.objects.get(id=1).number

@register.simple_tag()
def get_contact_info_mail_address():
    return Contact_informations.objects.first().mail_address

@register.simple_tag()
def get_contact_info_mail_telegramm():
    return Contact_informations.objects.first().telegramm

@register.simple_tag()
def get_all_contact_info():
    contact_info = cache.get('contact_ifno')
    if not contact_info:
        contact_info = Contact_informations.objects.first()
        cache.set('contact_ifno', contact_info, 60*60)

    return contact_info