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
    subject = f'Order #{order.id}'
    message = f'Dear {order.name},\n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                            message,
                            'settings.DEFAULT_FROM_EMAIL', # the sender / from address
                            [order.email]) # recipient address
    return mail_sent