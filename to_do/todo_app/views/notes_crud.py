from django.shortcuts import render


@login_required(login_url='/')
def save_note(request):
    notas = Notes.objects.filter(user_id = request.user.id)
    context={
        'listado' : notas,
        'usuario': request.user.first_name+" "+request.user.last_name
    }
    return render_to_response('todo.html',context)