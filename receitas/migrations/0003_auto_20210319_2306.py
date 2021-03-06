# Generated by Django 3.1.7 on 2021-03-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_auto_20210319_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='fast_recipe',
            field=models.BooleanField(default=False, verbose_name='receita rapida'),
        ),
        migrations.AddField(
            model_name='receitas',
            name='preparation_time',
            field=models.CharField(default=0, max_length=10, verbose_name='tempo de preparo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receitas',
            name='simple_recipe',
            field=models.BooleanField(default=False, verbose_name='receita simples'),
        ),
        migrations.AlterField(
            model_name='receitas',
            name='author',
            field=models.CharField(max_length=255, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='receitas',
            name='recipe',
            field=models.TextField(verbose_name='receita'),
        ),
        migrations.AlterField(
            model_name='receitas',
            name='title',
            field=models.CharField(max_length=255, verbose_name='titulo'),
        ),
    ]
