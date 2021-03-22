from django.db import models
from uuid import uuid4


class Receitas(models.Model):
    id_recipe = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.CharField('autor', max_length=255)
    title = models.CharField('titulo', max_length=255)
    recipe = models.TextField('receita')
    preparation_time = models.CharField('tempo de preparo', max_length=50)
    simple_recipe = models.BooleanField('receita simples', default=False)
    fast_recipe = models.BooleanField('receita rapida', default=False)
    create_at = models.DateField(auto_now_add=True)
