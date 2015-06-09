from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from todo_app.models import *
from django.http import *


@login_required(login_url='/')
def save_note(request):
    print request.POST['note_content']
    note = Notes.objects.create(note_content=request.POST['note_content'],user_id=request.user.id)
    return HttpResponseRedirect('/notes/')