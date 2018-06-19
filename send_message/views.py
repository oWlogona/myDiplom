from django.shortcuts import render
from .models import Dialog, Message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def create_dialog(request, user_id):
    if request.user.is_authenticated:
        user_1 = User.objects.get(id=request.user.id)
        user_2 = User.objects.get(id=user_id)
        dialog_id = Dialog.objects.filter(user_1=user_1, user_2=user_2)
        if not dialog_id:
            dialog_id = Dialog.objects.create(user_1=user_1, user_2=user_2)

        dialog_id = Dialog.objects.get(user_1=user_1, user_2=user_2)
        dialog_id = dialog_id.id
        url = '/dialog/' + str(dialog_id) + '/'
        return HttpResponseRedirect(url)
    else:
        print('read again')
    return render(request, 'my_profile.html', locals())


@login_required
def dialog(request, dialog_id):
    if request.user.is_authenticated:
        messages = Message.objects.all()
        print(messages)
        if request.method == 'POST':
            sender = request.user
            data_text = request.POST['message']
            Message.objects.create(sender=sender, text_message=data_text, dialog=dialog_id)
            dialog_id = Message.objects.get(dialog=dialog_id)
            dialog_id = dialog_id.id
            return render(request, 'room_page.html', locals())
    else:
        print('read again')
    return render(request, 'room_page.html', locals())
