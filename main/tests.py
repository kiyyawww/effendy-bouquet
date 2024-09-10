from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_name_user(self):
        product = Product.objects.create(
            name = "Buket Bunga",
            price = 65000,
            description = "Buket bunga dengan basic bunga mawar dan bisa di mix dengan jenis bunga yang lainnya",
            quantity = 10
        )
        self.assertTrue(product)