from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.celery import app
from django.core.mail import send_mail
#from django.conf import settings
from .models import Order

@shared_task
def order_created(order_id):
    """
    Task to send e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Commande N°{order.id}'
    message = f'{order.name},\n\n' \
                f'Vous avez passé votre commande avec succès. \n' \
                f'Le numéro de la commande est le suivant {order.id}.'
    mail_sent = send_mail(subject,
                            message,
                            'settings.DEFAULT_FROM_EMAIL', # the sender / from address
                            [order.customer]) # recipient address
    return mail_sent