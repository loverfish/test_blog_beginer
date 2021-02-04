from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_reverse(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/home.html')

class SignUpTests(TestCase):
    username = 'testuser'
    email = 'qwe@mail.ru'

    def test_signup_exist(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)



