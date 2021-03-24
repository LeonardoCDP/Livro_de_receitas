from django.test import TransactionTestCase

from receitas.models import Receitas


class ModelTestCase(TransactionTestCase):
    'this class tests Model'

    def setUp(self):
        self.obj = Receitas(
            author="Francis",
            title="Gelatina",
            recipe="Pegue uma gelatina\r\nFerva 250ml de agua quente\r\nAdicione",
            preparation_time="5 minutos",
            simple_recipe=True,
            fast_recipe=True,
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Receitas.objects.exists())

    def test_str(self):
        self.assertEqual('Francis', str(self.obj.author))

    def test_simple_recipe(self):
        self.assertEqual(True, self.obj.simple_recipe)
