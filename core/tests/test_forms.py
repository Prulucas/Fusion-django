from django.test import TestCase
from core.forms import ContactForm
from model_mommy import mommy


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Pedro Lucas'
        self.email = 'plbrandsilva@gmail.com'
        self.subject = 'Teste de form'
        self.message = 'Estou testando o meu form no arquivo test_form'

        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        # mesma coisa que realizar um POST
        self.form = ContactForm(data=self.data)

    def test_send_mail(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)
