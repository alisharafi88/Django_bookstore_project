from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SingUpPageTest(TestCase):
    user_name = 'myusername'
    email = 'myusername@gmail.com',

    def test_singup_url_by_name(self):
        response = self.client.get(reverse('sing_up'))
        self.assertEqual(response.status_code, 200)
    def test_singup_url(self):
        response = self.client.get('/accounts/singup/')
        self.assertEqual(response.status_code, 200)

    def test_singup_form(self):
        user = get_user_model().objects.create_user(
            self.user_name,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.user_name)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
