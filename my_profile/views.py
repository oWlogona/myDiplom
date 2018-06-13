from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .models import Profile
from .forms import ProfileForm


def get_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        print('read again')
    return render(request, 'my_profile.html', locals())


def show_my_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        user_check = Profile.objects.filter(user__username=user_name)
        print(user_check)
        if user_check:
            user = Profile.objects.get(user=request.user)
        else:
            print('not')
    return render(request, 'profile_user.html', locals())


def update_my_profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        print('ok')
        form = ProfileForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
        	form.save()
    else:
        print('read again')
    return render(request, 'update_profile.html', locals())


def logout_profile(request):
    logout(request)
    url = '/login_user/'
    return HttpResponseRedirect(url)
