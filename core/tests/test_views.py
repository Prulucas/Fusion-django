from django.test import TestCase, Client
from django.urls import reverse_lazy

# um pouco mais complexo que as outas


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Pedro Lucas',
            'email': 'plbrandsilva@gmail.com',
            'subject': 'Teste de views',
            'message': 'Testando a minha IndexView'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        invalid_data = {
            'name': 'Yasmin de Oliveira',
            'subject': 'Teste da função invalida'
        }
        request = self.client.post(reverse_lazy('index'), data=invalid_data)
        self.assertEqual(request.status_code, 200)
