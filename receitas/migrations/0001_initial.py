# Generated by Django 3.1.7 on 2021-03-20 00:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id_receita', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('receita', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
