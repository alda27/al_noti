from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from news.models import News
from .forms import UserEditForm, ProfileEditForm


@login_required()
def dashboard(request):
    user_save_news = News.published.all().filter(user_save=request.user)
    context = {'user_save_news': user_save_news}
    return render(request, 'account/dashboard.html', context)


@login_required()
def edit(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save(commit=False)
            profile_edit_form.user = user_edit_form
            if 'photo' in request.FILES:
                profile_edit_form.photo = request.FILES['photo']
            profile_edit_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito')
            return redirect('account:dashboard')
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)

    context = {'user_form': user_edit_form,
               'profile_form': profile_edit_form}
    return render(request, 'account/edit.html', context)


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        next_parameter = request.POST['next']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El usuario ya existe')
                redirect('account:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El email ya existe')
                redirect('account:register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password)
                user.save()
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                if next_parameter:
                    return redirect(next_parameter)
                messages.success(request, 'Registro exitoso')
    return render(request, 'account/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_parameter = request.POST['next']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_parameter:
                return redirect(next_parameter)
            return redirect('home:home')
        else:
            messages.error(request, 'Las credenciales no son correctas. intentalo de nuevo')
            return redirect('account:login')
    return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    return redirect('home:home')
