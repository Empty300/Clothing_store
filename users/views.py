from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from common.views import CommonMixin
from orders.models import Order
from users.forms import (RegisterForm, UserLoginForm, UserProfileForm,
                         UserResetPassForm)
from users.models import User
from users.services import send_email_for_reset_pass


class UserLoginView(CommonMixin, LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Giant - Войти'


class UserRegistrationView(CommonMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    title = 'Giant - Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('store:index_page')


class UserProfileView(CommonMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/account.html'
    title = 'Giant - Личный кабинет'

    def get(self, request, *args, **kwargs):
        if self.request.user.pk != self.kwargs['pk']:
            return HttpResponseRedirect(reverse('index'))
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['orders'] = Order.objects.filter(initiator=self.request.user).order_by('-id')
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


def password_reset(request):
    title = 'Giant - сброс пароля'
    if request.method == 'GET':
        form = UserResetPassForm()
        context = {'form': form,
                   'title': title}
    else:
        context = send_email_for_reset_pass(request, title)
    return render(request, 'users/forgot-password.html', context)


class PasswordResetView(CommonMixin, SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'users/new_password.html'
    success_message = "Пароль успешно изменен"
    success_url = reverse_lazy("users:login")
    title = 'Giant - Сброс пароля'
