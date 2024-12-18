from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Q
from .models import Game
from .serializers import GameSerializer
from .schema import (
    get_game_schema,
    get_games_schema,
    get_recommended_games_schema,
    create_game_schema,
    update_game_schema,
    delete_game_schema,
)

"""
Retrieve a single game by ID or name.

Parameters:
    request: HTTP request object
        Query Parameters:
            id (optional): The unique identifier of the game to retrieve
            name (optional): The name of the game to search for (case-insensitive partial match)

Returns:
    Response object with:
        - Game data if found
        - HTTP 200 if successful
        - HTTP 400 if neither id nor name parameter is provided
        - HTTP 404 if no game matches the provided id or name
"""


@get_game_schema()
@api_view(["GET"])
def get_game(request):
    pk = request.query_params.get("id")
    name = request.query_params.get("name")

    if not pk and not name:
        return Response(
            {"message": "Please provide either id or name parameter"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        if pk:
            game = Game.objects.get(pk=pk)
        else:
            game = Game.objects.filter(name__icontains=name).first()
            if not game:
                raise Game.DoesNotExist
    except Game.DoesNotExist:
        return Response(
            {"message": "Game does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = GameSerializer(game)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""
Create a new game with the provided data.

Parameters:
    request: HTTP request object
        Body: JSON object containing game data
            Required fields:
                - name: Game title
                - release_date: Release date (YYYY-MM-DD)
                - price: Game price (decimal)
            Optional fields:
                - All other Game model fields

Returns:
    Response object with:
        - message: Success message
        - game: Complete created game object
        - HTTP 201 if successfully created
        - HTTP 400 if validation fails with error details
"""


@create_game_schema()
@api_view(["POST"])
def create_game(request):
    serializer = GameSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Game created successfully", "game": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Update an existing game by ID or name.

Parameters:
    request: HTTP request object
        Query Parameters:
            id (optional): The unique identifier of the game to update
            name (optional): The name of the game to update (case-insensitive partial match)
        Body: JSON object containing fields to update

Returns:
    Response object with:
        - message: Success message
        - game: Complete updated game object
        - HTTP 200 if successful
        - HTTP 400 if validation fails or no id/name provided
        - HTTP 404 if game not found
"""


@update_game_schema()
@api_view(["PATCH"])
def update_game(request):
    pk = request.query_params.get("id")
    name = request.query_params.get("name")

    if not pk and not name:
        return Response(
            {"message": "Please provide either id or name parameter"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        if pk:
            game = Game.objects.get(pk=pk)
        else:
            game = Game.objects.filter(name__icontains=name).first()
            if not game:
                raise Game.DoesNotExist
    except Game.DoesNotExist:
        return Response(
            {"message": "Game does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = GameSerializer(game, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Game updated successfully", "game": serializer.data},
            status=status.HTTP_200_OK,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Delete a game by ID or name.

Parameters:
    request: HTTP request object
        Query Parameters:
            id (optional): The unique identifier of the game to delete
            name (optional): The name of the game to delete (case-insensitive partial match)

Returns:
    Response object with:
        - message: Success message
        - HTTP 204 if successfully deleted
        - HTTP 400 if no id/name provided
        - HTTP 404 if game not found
"""


@delete_game_schema()
@api_view(["DELETE"])
def delete_game(request):
    pk = request.query_params.get("id")
    name = request.query_params.get("name")

    if not pk and not name:
        return Response(
            {"message": "Please provide either id or name parameter"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        if pk:
            game = Game.objects.get(pk=pk)
        else:
            game = Game.objects.filter(name__icontains=name).first()
            if not game:
                raise Game.DoesNotExist
    except Game.DoesNotExist:
        return Response(
            {"message": "Game does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    game.delete()
    return Response(
        {"message": "Game deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


"""
Get a paginated list of games with optional filtering and sorting.

Parameters:
    request: HTTP request object
        Query Parameters:
            filterBy (optional): Filter games using the following syntax:
                - genre(Action,RPG): Filter by one or more genres (comma-separated)
                - platform(windows,mac,linux): Filter by one or more platforms (comma-separated)
                - year(2021,2022): Filter by one or more release years (comma-separated)
                Multiple filters can be combined, e.g. "genre(Action)&platform(windows,mac)"
            
            sortBy (optional): Sort results by one of:
                - metacriticScore: Sort by Metacritic score
                - price: Sort by game price
                - releaseDate: Sort by release date
            
            sortOrder (optional): Sort direction
                - asc: Ascending order
                - desc: Descending order (default)
            
            page (optional): Page number for pagination (default: 1)
            pageSize (optional): Number of results per page (default: 100, max: 100)

Returns:
    Response object with:
        - count: Total number of matching results
        - next: URL for next page of results (null if none)
        - previous: URL for previous page (null if none)
        - results: Array of games for current page
        - HTTP 200 if successful
"""


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "pageSize"
    max_page_size = 100


@get_games_schema()
@api_view(["GET"])
def get_games(request):
    paginator = StandardResultsSetPagination()
    games = Game.objects.all()

    # Process filterBy parameter to filter games by genre, platform and year
    filter_by = request.query_params.get("filterBy", "")
    if filter_by:
        # Filter by genre - matches games containing any of the specified genres
        if "genre(" in filter_by:
            genres = filter_by.split("genre(")[1].strip(")").split(",")
            genres_query = None
            for genre in genres:
                if genres_query is None:
                    genres_query = Q(genres__icontains=genre.strip())
                else:
                    genres_query |= Q(genres__icontains=genre.strip())
            if genres_query:
                games = games.filter(genres_query)

        # Filter by platform - matches games available on any of the specified platforms
        if "platform(" in filter_by:
            platforms = filter_by.split("platform(")[1].strip(")").split(",")
            platform_query = None
            for platform in platforms:
                platform = platform.strip().lower()
                if platform == "windows":
                    new_query = Q(windows=True)
                if platform == "mac":
                    new_query = Q(mac=True)
                if platform == "linux":
                    new_query = Q(linux=True)
                else:
                    continue

                if platform_query is None:
                    platform_query = new_query
                else:
                    platform_query |= new_query
            if platform_query:
                games = games.filter(platform_query)

        # Filter by release year - matches games released in any of the specified years
        if "year(" in filter_by:
            years = filter_by.split("year(")[1].strip(")").split(",")
            year_query = None
            for year in years:
                if year_query is None:
                    year_query = Q(release_date__year=year.strip())
                else:
                    year_query |= Q(release_date__year=year.strip())
            if year_query:
                games = games.filter(year_query)

    # Apply sortBy parameter to sort games by metacritic_score, price and release_date
    # Apply sortOrder parameter to sort direction, either 'asc' or 'desc' (default: desc)
    sort_by = request.query_params.get("sortBy", "")
    sort_order = request.query_params.get("sortOrder", "desc").lower()

    if sort_by:
        sort_field = ""
        if sort_by.lower() == "metacriticscore":
            sort_field = "metacritic_score"
        if sort_by.lower() == "price":
            sort_field = "price"
        if sort_by.lower() == "releasedate":
            sort_field = "release_date"

        if sort_field:
            if sort_order == "asc":
                games = games.order_by(sort_field)
            else:
                games = games.order_by(f"-{sort_field}")

    # Paginate and serialize the filtered/sorted results
    result_page = paginator.paginate_queryset(games, request)
    serializer = GameSerializer(result_page, many=True)

    return Response(
        paginator.get_paginated_response(serializer.data).data,
        status=status.HTTP_200_OK,
    )


"""
Get recommended games based on similarity to a reference game.

Parameters:
    request: HTTP request object
        Query Parameters:
            id (optional): The unique identifier of the reference game
            name (optional): The name of the reference game (case-insensitive partial match)

Returns:
    Response object with:
        - reference_game: Name of the game used as reference
        - similar_games: List of up to 5 similar games, sorted by similarity score
        - HTTP 200 if successful
        - HTTP 400 if neither id nor name provided
        - HTTP 404 if reference game not found

Similarity scoring algorithm:
    Games are scored based on matching attributes with the following weights:
    - Each matching genre: 3 points
    - Each matching tag: 2 points
    - Each matching category: 1 point
    
    Games are ranked by total score and only those with score > 0 are included.
    The top 5 highest scoring games are returned as recommendations.
"""


@get_recommended_games_schema()
@api_view(["GET"])
def get_recommended_games(request):
    pk = request.query_params.get("id")
    name = request.query_params.get("name")

    if not pk and not name:
        return Response(
            {"message": "Please provide either id or name parameter"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        # Get the reference game
        if pk:
            reference_game = Game.objects.get(pk=pk)
        else:
            reference_game = Game.objects.filter(name__icontains=name).first()
            if not reference_game:
                raise Game.DoesNotExist

        # Get reference game attributes
        ref_genres = set(g.genre for g in reference_game.genres.all())
        ref_tags = set(t.tag for t in reference_game.tags.all())
        ref_categories = set(c.category for c in reference_game.categories.all())

        # Get all other games
        all_other_games = Game.objects.exclude(pk=reference_game.pk)

        # Score each game based on similarities
        scored_games = []
        for game in all_other_games:
            score = 0

            # Genre matching (weight: 3)
            game_genres = set(g.genre for g in game.genres.all())
            matching_genres = len(ref_genres & game_genres)
            score += matching_genres * 3

            # Tag matching (weight: 2)
            game_tags = set(t.tag for t in game.tags.all())
            matching_tags = len(ref_tags & game_tags)
            score += matching_tags * 2

            # Category matching (weight: 1)
            game_categories = set(c.category for c in game.categories.all())
            matching_categories = len(ref_categories & game_categories)
            score += matching_categories

            if score > 0:  # Only include games with some similarity
                scored_games.append((score, game))

        # Sort by score and get top 5
        scored_games.sort(key=lambda x: x[0], reverse=True)
        similar_games = [game for score, game in scored_games[:5]]

        serializer_reference_game = GameSerializer(reference_game)
        serializer_similar_games = GameSerializer(similar_games, many=True)

        return Response(
            {
                "reference_game": serializer_reference_game.data,
                "recommended_games": serializer_similar_games.data,
            },
            status=status.HTTP_200_OK,
        )

    except Game.DoesNotExist:
        return Response(
            {"message": "Game does not exist"}, status=status.HTTP_404_NOT_FOUND
        )
