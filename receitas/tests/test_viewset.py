from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from receitas.api.serializers import ReceitasSerializer
from receitas.models import Receitas


class RecipeTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "author": "Francis",
            "title": "Gelatina",
            "recipe": "Pegue uma gelatina\r\nFerva 250ml de agua quente\r\nAdicione",
            "preparation_time": "5 minutos",
            "simple_recipe": True,
            "fast_recipe": True}
        url = reverse('recipe-create')
        self.resp = self.client.post(url, self.data, format='json')
        serializer = ReceitasSerializer(Receitas.objects.get(), many=False)
        self.id_recipe = serializer.data['id_recipe']

    def test_post(self):
        self.assertEqual(self.resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Receitas.objects.count(), 1)
        self.assertEqual(Receitas.objects.get().author, 'Francis')


    def test_get_recipe_list(self):
        resp = self.client.get('/recipe-list/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        resp = self.client.get(f'/recipe-detail/{self.id_recipe}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_recipe_detail_author(self):
        author = "Francis"
        resp = self.client.get(f'/recipe-detail-author/{author}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_recipe_detail_title(self):
        title = "Gelatina"
        resp = self.client.get(f'/recipe-detail-title/{title}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_recipe_fast_and_simple(self):
        resp = self.client.get('/recipe-fast-and-simple/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_recipe_fast_and_simple_and_title(self):
        title = "Gelatina"
        resp = self.client.get(f'/recipe-fast-and-simple-and-title/{title}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_recipe_update(self):
        author = {

                    "author": "John",
                    "title": "Gelatina",
                    "recipe": "Pegue uma gelatina\r\nFerva 250ml de agua quente\r\nAdicione a gelatina e misture ate dissolver\r\nAdicione 250ml de agua fria\r\nleve a geladeira ate ficar firme\r\nagora e só servir",
                    "preparation_time": "5 minutos",
                    "simple_recipe": True,
                    "fast_recipe": True

                }
        resp = self.client.put(f'/recipe-update/{self.id_recipe}/', author)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(Receitas.objects.get().author, 'John')

    def test_recipe_delete(self):
        resp = self.client.delete(f'/recipe-delete/{self.id_recipe}/')
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Receitas.objects.count(), 0)