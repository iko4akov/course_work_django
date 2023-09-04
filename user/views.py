from random import randint

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from services.generate_password import generate_password
from services.send_email import send_email
from user.forms import UserRegisterForm, UserProfile
from user.models import User


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    fields = '__all__'
    permission_required = 'user.view_user'



class RegistertView(CreateView):
    model = User
    form_class = UserRegisterForm

    template_name = 'user/register.html'

    success_url = reverse_lazy('user:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfile
    template_name = 'user/user_form.html'

    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user


def check_email(request):
    context = {}
    user = request.user
    if request.method == 'GET':
        verify_number = randint(0, 99999)
        user.verify_number = verify_number
        email = user.email
        send_email(email, verify_number)
        user.save()
        context = {'object': user}
    if request.method == 'POST':
        code = user.verify_number
        entered_code = request.POST.get('code')
        if str(entered_code) == str(code):
            user.check_email = True
            user.save()
            return render(template_name='frontend/list.html', request=request)
        else:
            context['error'] = 'Неверный код'
            return render(template_name='user/check_email.html', request=request, context=context)

    return render(template_name='user/check_email.html', request=request, context=context)


def password(request):
    context = {}
    if request.method == 'POST':
        password = generate_password()
        email = request.POST.get('email')
        info = 'Востановление пароля, ваш новый пароль: '
        send_email(email, password, info)
        try:
            user = User.objects.get(email=f'{email}')
            user.set_password(password)
            user.save()
            return render(request, template_name='frontend/list.html', context=context)

        except Exception:

            context = {'error': 'Пользователь с таким email не зарегистрирован'}
            return render(request, template_name='user/password.html', context=context)

    return render(request, template_name='user/password.html')

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user:delete')
    permission_required = 'user.delete_user'
