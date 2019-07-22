from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_email


class UserinfoView(View):
    pass


class UploadImageView(View):
    pass


class UpdatePwdView(View):
    pass


class SendEmailCodeView(View):
    pass


class UpdateEmailView(View):
    pass


class MyCourseView(View):
    pass


class MyFavOrgView(View):
    pass


class MyFavTeacherView(View):
    pass


class MyFavCourseView(View):
    pass


class MymessageView(View):
    pass


class LogoutView(View):
    pass


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
            else:
                raise Exception('no such user')
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_active:
                    return render(request, 'login.html', {'msg': 'The user is not activated.'})
                else:
                    login(request, user)
                    return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': 'wrong username or password.'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'msg': 'This email already registered.'})
            else:
                password = request.POST.get('password', '')
                pwd = make_password(password)
                user = UserProfile()
                user.email = email
                user.username = email
                user.password = pwd
                user.is_active = False
                user.save()

                send_register_email(email, 'register')
                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        records = EmailVerifyRecord.objects.filter(code = active_code)
        if records:
            for record in records:
                user = UserProfile.objects.get(email=record.email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email":email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    """
    修改用户密码
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致"})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return redirect('login')
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form})



