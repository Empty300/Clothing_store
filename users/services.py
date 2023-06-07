from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.forms import UserResetPassForm
from users.models import User


def send_email_for_reset_pass(request, title):
    """Проверяет существование пользователя. Отправляет email со ссылкой для сброса пароля"""
    form = UserResetPassForm()
    try:
        user = User.objects.get(email=request.POST["email"])
    except User.DoesNotExist:
        user = False
    if user:
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        link = f'/users/password_reset/new_pass/{uid}/{token}/'
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Сброс пароля для {user.username}'
        message = 'Для сброса пароля {} перейдите по ссылке: {}'.format(
            request.user.username,
            verification_link
        )
        html_message = loader.render_to_string(
            'users/email_reset_pass.html',
            {
                'user_name': user.username,
                'verification_link': verification_link,
            }
        )
        send_mail(
            subject=subject,
            html_message=html_message,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(user.email,),
            fail_silently=False,
        )
        context = {'msg': 'Письмо с ссылкой для сброса пароля отправлено вам на почту',
                   'form': form,
                   'title': title}
    else:
        context = {'msg': 'Пользователь с таким email не найден',
                   'form': form,
                   'title': title}
    return context
