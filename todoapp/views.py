from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseBadRequest

from .models import User, Note
from .serializers import UserSerializer, NoteSerializer


# REST API ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Template Views
@csrf_protect
def note_list(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.POST.get('user')

        user = None
        if user_id == '1':
            user, _ = User.objects.get_or_create(id=1, defaults={'name': '관리자'})
        elif user_id == '2':
            user, _ = User.objects.get_or_create(id=2, defaults={'name': '고객'})


        Note.objects.create(title=title, content=content, user=user)
        return redirect('note_list')

    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'todoapp/note_list.html', {'notes': notes})

@csrf_protect
def note_delete(request, note_id):
    if request.method != 'POST':
        return HttpResponseBadRequest("잘못된 요청입니다.")

    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('note_list')

