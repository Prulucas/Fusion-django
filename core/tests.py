from django.test import TestCase

# Create your tests here.


def add_num(num):
    return num + 1


class SimpleTestCase(TestCase):

    # roda sempre
    def setUp(self):
        self.numero = 41
        print('Iniciando o TestCase')

    # Testa a unidade de código:
    def test_add_num(self):
        value = add_num(self.numero)
        self.assertTrue(value == 42)


# Todo teste, começa com "test_"
'''
    Para executar o teste é preciso  estar no mesmo diretorio que o manage.py no terminal e rodar o comando
    'python manage.py test', se retornar 'Ok', Se falhar ele fala a linha que deu erro e o nome do teste
    Para organizar melhor deve-se deletar esse arquivo tests e criar um diretório de 'tests'
'''
