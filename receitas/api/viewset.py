from .serializers import ReceitasSerializer
from receitas.models import Receitas
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    '''EndPoints list'''
    api_urls = {
        'List': '/recipe-list/',
        'Detail View': '/recipe-detail/<str:uuid4>/',
        'Detail View Chef': '/recipe-detail-author/<str:author>/',
        'Detail View Title': '/recipe-detail-title/<str:title>/',
        'Detail View Simple And Fast Recipe': '/recipe-fast-and-simple/',
        'Detail View Simple And Fast Recipe And Title':
            '/recipe-fast-and-simple/<str:title>/',
        'Create': '/recipe-create/',
        'Update': '/recipe-update/<str:uuid4>/',
        'Delete': '/recipe-delete/<str:uuid4>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def recipeListe(request):
    '''Endpoint return all items in data'''
    recipe = Receitas.objects.all()
    serializers = ReceitasSerializer(recipe, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def recipeDetail(request, uuid4):
    '''Endpoint search and return item by ID'''
    recipe = getRecipeId(uuid4)
    serializer = ReceitasSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def recipeDetailAuthor(request, author):
    '''Endpoint search and return item(s) by author'''
    try:
        recipe = Receitas.objects.all().filter(author=author)
    except Receitas.DoesNotExist:
        return Response(status=404)

    serializer = ReceitasSerializer(recipe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipeDetailTitle(request, title):
    '''Endpoint search and return item(s) by title (recipe)'''
    try:
        recipe = Receitas.objects.all().filter(title=title)
    except Receitas.DoesNotExist:
        return Response(status=404)

    serializer = ReceitasSerializer(recipe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipeDetailSimpleAndFast(request):
    '''Endpoint return item(s) by simple and fast recipe'''
    try:
        recipe = Receitas.objects.all().filter(simple_recipe=True,
                                               fast_recipe=True)
    except Receitas.DoesNotExist:
        return Response(status=404)

    serializer = ReceitasSerializer(recipe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipeDetailSimpleAndFastAndTitle(request, title=None):
    '''Endpoint search and return item(s) by simple and fast and title (recipe)'''
    try:
        recipe = Receitas.objects.all().filter(simple_recipe=True,
                                               fast_recipe=True).filter(title=title)
    except Receitas.DoesNotExist:
        return Response(status=404)

    serializer = ReceitasSerializer(recipe, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def recipeCreate(request):
    '''Endpoint  create recipe data'''
    serializer = ReceitasSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def recipeUpdate(request, uuid4):
    '''Endpoint  update recipe by ID'''
    recipe = getRecipeId(uuid4)
    serializer = ReceitasSerializer(instance=recipe, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def recipeDelete(request, uuid4):
    '''Endpoint  delete recipe by ID'''
    recipe = getRecipeId(uuid4)
    recipe.delete()
    return Response('Item succesfully delete', status=status.HTTP_204_NO_CONTENT)


def getRecipeId(uuid4):
    '''Search object by ID and return object'''
    try:
        return Receitas.objects.get(id_recipe=uuid4)
    except Receitas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
