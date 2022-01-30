import datetime
from django.test import TestCase, Client
from tinyapp.models import User, Url

class Test(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Katherine",
            last_name="Johnson",
            username="KJ",
            email="mathematics@nasa.com",
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password("!P4s5w0*d")
        self.user.save()
        self.url1 = Url.objects.create(
            short_url='cZnrp8',
            long_url='https://www.bbc.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url2 = Url.objects.create(
            short_url='bx2Vn2',
            long_url='https://www.google.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url3 = Url.objects.create(
            short_url='nCo1w8',
            long_url='https://www.cbc.ca',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url4 = Url.objects.create(
            short_url='wxBIh9',
            long_url='https://www.youtube.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        self.url5 = Url.objects.create(
            short_url='bQJscc',
            long_url='https://www.netflix.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
    def test_login_list_view_logged_in(self):
        c = Client()
        login_response = c.post('/login/',{'username':'KJ', 'password':'!P4s5w0*d'})
        login_check = c.get('/login/')
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, '/urls')
        self.assertEqual(login_check.status_code, 200)
    
    def test_register(self):
        c = Client()
        login_response = c.post('/login/',{'username':'KJ', 'password':'!P4s5w0*d'})
        login_check = c.get('/register/')
        self.assertEqual(login_check.status_code, 200)
    
    def test_short_urls(self):
        c = Client()
        login_response = c.post('/login/',{'username':'KJ', 'password':'!P4s5w0*d'})
        login_check = c.get('/urls/u/<short_url>')
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_check.status_code, 301)

    