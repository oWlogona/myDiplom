from django.shortcuts import render
from .models import Dialog, Message
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def create_dialog(request, user_id):
    if request.user.is_authenticated:
        dialog_id = Dialog.objects.filter(
            user_1=request.user.id, user_2=user_id)
        if not dialog:
            dialog_id = Dialog.objects.create(
                user_1=request.user.id, user_2=user_id)
            url = '/dialog/' + str(dialog_id) + '/'
            return HttpResponseRedirect(url)
        url = '/dialog/' + str(dialog_id) + '/'
        return HttpResponseRedirect(url)
    else:
        print('read again')
    return render(request, 'my_profile.html', locals())


@login_required
def dialog(request, dialog_id):
    pass
    
