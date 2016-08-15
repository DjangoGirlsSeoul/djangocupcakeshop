from django.test import TestCase
from .models import Cupcake
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class MenuTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Cupcake.objects.create(name="chocolate",rating=5, writer=u,price="20")
        Cupcake.objects.create(name="earl grey",rating=4, writer=u,price="10")

    def test_cupcake_has_name(self):
        """Menu Test
            Fields tested : name,rating,writer
        """
        cupcake1 = Cupcake.objects.get(name="chocolate")
        cupcake2 = Cupcake.objects.get(name="earl grey")
        self.assertEqual(cupcake1.name, 'chocolate')
        self.assertEqual(cupcake1.rating, 5)
        self.assertEqual(cupcake2.price, '10')
        self.assertEqual(cupcake1.price, '20')

# uncomment this code in Step 9
# class MenuTestiView(TestCase):
#     def test_index_view_with_no_cupcake(self):
#         """
#         If no cupcakes exist, an appropriate message should be displayed
#         """
#         response = self.client.get(reverse('menu:cupcake_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No Cupcakes added yet")
