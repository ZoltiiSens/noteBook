from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user


class ViewTestClass(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='test1', password='test1')
        test_user1.save()

    def test_home_exist_at_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')

    def test_home_exist_at_location_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')

    def test_signup_exist_at_location(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')

    def test_signup_exist_at_location_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')

    def test_signup_with_correct_data(self):
        response = self.client.post(reverse('signup'), {'username': 'test2', 'password1': 'test2', 'password2': 'test2'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/week_list/')
        user = get_user(self.client)
        self.assertEqual(user, User.objects.get(username='test2'))

    def test_signup_with_no_mached_passwords(self):
        response = self.client.post(reverse('signup'), {'username': 'test2', 'password1': 'test2', 'password2': 'test3'})
        self.assertEqual(response.status_code, 200)
        user = get_user(self.client)
        self.assertEqual(str(user), 'AnonymousUser')

    def test_login_exist_at_location(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_exist_at_location_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_with_correct_data(self):
        response = self.client.post(reverse('login'), {'username': 'test1', 'password': 'test1'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/week_list/')
        user = get_user(self.client)
        self.assertEqual(user, User.objects.get(username='test1'))

    def test_signup_with_incorrect_data(self):
        response = self.client.post(reverse('login'), {'username': 'test2', 'password': 'test2'})
        self.assertEqual(response.status_code, 200)
        user = get_user(self.client)
        self.assertEqual(str(user), 'AnonymousUser')

    def test_logout_redirect_if_not_authenticated(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/login/?next=/logout/')

    def test_logout_redirect_if_authenticated(self):
        self.client.login(username='test1', password='test1')
        response = self.client.post('/logout/', {})
        self.assertTrue(response.context is None)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
