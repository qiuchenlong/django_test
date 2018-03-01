from django.test import TestCase

# Create your tests here.


from django.test import TestCase, Client
from polls.models import Person

class PersonTestCase(TestCase):

    def setUp(self):
        pass
        # Person.objects.create(first_name="qq", last_name="wx")
        # Person.objects.create(first_name="xl", last_name="wb")

    def test_animals_can_speak(self):
        # qq = Person.objects.get(first_name="qq")
        # xl = Person.objects.get(first_name="xl")
        # self.assertEqual(qq.speak(), "The qq says wx")
        # self.assertEqual(xl.speak(), "The xl says wb")
        c = Client()
        resp = c.get("/polls", {"id": 2})
        # print("aaa", resp.status_code, resp.content_params)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '{"id": "2"}')