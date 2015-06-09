from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from todo_app.models import *
from django.shortcuts import render


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/notes/')
    return render(request,'login.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def notas(request):
    notas = Notes.objects.filter(user_id = request.user.id)
    context={
        'listado' : notas,
        'usuario': request.user.first_name+" "+request.user.last_name
    }
    return render(request,'todo.html',context)