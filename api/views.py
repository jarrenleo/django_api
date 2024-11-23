from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Game
from .serializers import GameSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def get_games(request):
    paginator = StandardResultsSetPagination()
    games = Game.objects.all()
    result_page = paginator.paginate_queryset(games, request)
    serializer = GameSerializer(result_page, many=True)

    return Response(paginator.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_game(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({"message": "Game does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = GameSerializer(game)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_top_rated_games(request):
    paginator = StandardResultsSetPagination()
    games = Game.objects.all().order_by('-metacritic_score')
    result_page = paginator.paginate_queryset(games, request)
    serializer = GameSerializer(result_page, many=True)

    return Response(paginator.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_games_by_year(request, year):
    paginator = StandardResultsSetPagination()
    games = Game.objects.filter(release_date__year=year)
    result_page = paginator.paginate_queryset(games, request)
    serializer = GameSerializer(result_page, many=True)

    return Response(paginator.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_game(request):
    serializer = GameSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_game(request, pk):
    game = Game.objects.get(pk=pk)
    serializer = GameSerializer(game, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_game(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({"message": "Game does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    game.delete()
    return Response({"message": "Game deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
