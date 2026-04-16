import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

# Testando as funções str:


class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = mommy.make('Services')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service_title)


class PositionTestCase(TestCase):
    def setUp(self):
        self.position = mommy.make('Position')

    def test_str(self):
        self.assertEqual(str(self.position), self.position.position)


class MemberTestCase(TestCase):
    def setUp(self):
        self.member = mommy.make('Member')

    def test_str(self):
        self.assertEqual(str(self.member), self.member.name)


class FeaturesTestCase(TestCase):
    def setUp(self):
        self.feature = mommy.make('Features')

    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.name)
