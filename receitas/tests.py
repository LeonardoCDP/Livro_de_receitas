import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Receitas
from receitas.api.serializers import ReceitasSerializer


class RecipeTestCase(APITestCase):

    def test_create(self):
        data = {"author": "Francis",
        "title": "Gelatina",
        "recipe": "Pegue uma gelatina\r\nFerva 250ml de agua quente\r\nAdicione",
        "preparation_time": "5 minutos",
        "fast_recipe": True}
        response = self.client.post('/recipe-create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)