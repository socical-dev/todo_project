from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Note


class NoteAppTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(name='홍길동', email='hong@test.com')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.name, '홍길동')

    def test_note_creation(self):
        Note.objects.create(title='테스트 메모', content='내용입니다.', user=self.user)
        self.assertEqual(Note.objects.count(), 1)

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Notes')

    def test_note_api_create(self):
        response = self.client.post('/api/notes/', {
            'title': 'API 메모',
            'content': 'API로 작성',
            'user': self.user.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Note.objects.count(), 1)
