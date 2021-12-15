from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse  # allow us to generate url for admin page


class AdminSiteTests(TestCase):

    def setUp(self):
        """function that is run before every test that we run"""
        self.client = Client()  #
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com', password='password123'
        )
        self.client.force_login(self.admin_user)  #
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com', password="password123",
            name="Test user full name"
        )

    def test_users_listed(self):
        """test that users are listed om the user page"""
        url = reverse('admin:coresapp_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse("admin:coresapp_user_change", args=[self.user.id])
        #admin/coresapp/user/id
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:coresapp_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)
