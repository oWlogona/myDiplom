from django.shortcuts import render

# Create your views here.


def send_message(request):
    if request.user.is_authenticated:
        user_name = request.user
    else:
        print('read again')
    return render(request, 'room_page.html', locals())
