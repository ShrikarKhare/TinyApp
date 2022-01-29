import datetime
from django.test import TestCase
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
        urls = []
        # for i in range(5):
        #     urls.append(
        #         self.url = Url.objects.create(
        #         short_url='bx2Vn2',
        #         long_url='https://www.google.com',
        #         user=self.user,
        #         date_created=datetime.datetime.now()
        #     )
            
        