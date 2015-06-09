from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from todo_app.models import *


@login_required(login_url='/')
def save_note(request):
    print request.POST['note_content']
    note = Note.objects.create(note_content=request.POST['note_content'])
    print note.pk