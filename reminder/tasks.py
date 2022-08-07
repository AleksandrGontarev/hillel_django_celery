from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send(email, text_reminder):

    send_mail(
        'Reminder',
        text_reminder,
        'gontarevsanya@gmail.com',
        [email, ],
        fail_silently=False,
    )
    pass
