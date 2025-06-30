from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NoteViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),  # REST API: /users/, /notes/
    path('note-page/', views.note_list, name='note_list'),  # HTML: /notes/
    path('note-page/delete/<int:note_id>/', views.note_delete, name='note_delete'),  # HTML: 삭제용
]
