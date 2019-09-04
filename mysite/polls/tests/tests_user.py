import datetime
import json
from django.test import TestCase
from django.test import Client
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from polls.models import Question


class QuestionModelTests(TestCase):
    databases = {'default',} # {'__all__',}
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='kapil_jain', email='kapiljain.jain93@gmail.com', password='Test@123')

#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=1)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)

    def test_get_user_failed(self):
        url = reverse('polls:get_user_by_contact')
        data = {'username': 'kapil_jain1'}
        response = self.c.get('/polls/reg-django/get-user/', data)
        self.assertEquals(response.status_code, 400)
        
        
    def test_get_user_success(self):
        url = reverse('polls:get_user_by_contact')
        data = {'username': 'kapil_jain'}
        response = self.c.get(url, data)
        rdata = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(rdata['username'], self.user.username)