# coding=utf-8

from django.core.mail import EmailMessage
from rest_framework.decorators import api_view

from .response import response_success, response_error


class TestView(object):
    @staticmethod
    @api_view(['GET'])
    def email_verify(request):
        try:
            mail = EmailMessage(u'Notificacion',
                                u'El contenedor esta lleno. ',
                                to=['piero.rau.e@gmail.com'])

            mail.send()
            return response_success(data='ok')
        except:
            return response_error(error='fail')
            # raise
