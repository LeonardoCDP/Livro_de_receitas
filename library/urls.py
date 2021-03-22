"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from receitas.api import viewset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewset.apiOverview, name='api-overview'),
    path('recipe-list/', viewset.recipeListe, name='recipe-list'),
    path('recipe-detail/<str:uuid4>/', viewset.recipeDetail, name='recipe-detail'),
    path('recipe-detail-author/<str:author>/', viewset.recipeDetailAuthor,
         name='recipe-detail-author'),
    path('recipe-detail-title/<str:title>/', viewset.recipeDetailTitle,
         name='recipe-detail-title'),
    path('recipe-fast-and-simple/', viewset.recipeDetailSimpleAndFast,
         name='recipe-fast-and-simple'),
    path('recipe-fast-and-simple-and-title/<str:title>/',
         viewset.recipeDetailSimpleAndFastAndTitle,
         name='recipe-fast-and-simple-and-title'),
    path('recipe-create/', viewset.recipeCreate, name='recipe-create'),
    path('recipe-update/<str:uuid4>/', viewset.recipeUpdate, name='recipe-update'),
    path('recipe-delete/<str:uuid4>/', viewset.recipeDelete, name='recipe-delete'),
]
