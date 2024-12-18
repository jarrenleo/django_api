from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import GameSerializer

"""
Swagger/OpenAPI schema definition for the get_game endpoint.

This schema documents the API endpoint that retrieves a single game by ID or name.
It specifies:
- HTTP method: GET
- Query parameters:
    - id (optional): Integer ID of the game to retrieve
    - name (optional): String name of the game to search for
- Response formats:
    - 200: Successful response with full game details including:
        - Basic info (name, release date, price)
        - Statistics (owners, peak users, playtime)
        - Content details (age rating, DLC count, description)
        - Platform support (Windows, Mac, Linux)
        - Languages (interface and audio)
        - Media (header image)
        - External links (website, support)
        - Ratings (Metacritic, user ratings)
        - Related entities (developers, publishers, genres, tags)
    - 400: Error when neither id nor name provided
    - 404: Error when game not found

Returns:
    swagger_auto_schema: Decorator configured with complete endpoint documentation
"""


def get_game_schema():
    return swagger_auto_schema(
        method="get",
        operation_description="Retrieve a single game by ID or name.",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="The unique identifier of the game",
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="The name of the game to search for",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": {
                        "id": 5504,
                        "name": "ELDEN RING",
                        "release_date": "2022-02-24",
                        "estimated_owners": 50000000,
                        "peak_concurrent_users": 46431,
                        "required_age": 16,
                        "price": "59.99",
                        "dlc_count": 0,
                        "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                        "supported_languages": [
                            "English",
                            "French",
                            "German",
                            "Polish",
                            "Russian",
                            "Italian",
                            "Japanese",
                            "Spanish - Spain",
                            "Korean",
                            "Portuguese - Brazil",
                            "Simplified Chinese",
                            "Traditional Chinese",
                            "Spanish - Latin America",
                            "Thai",
                        ],
                        "full_audio_languages": ["English", "Traditional Chinese"],
                        "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg",
                        "website": "",
                        "support_url": "https://www.bandainamcoent.com/support",
                        "support_email": "",
                        "windows": True,
                        "mac": False,
                        "linux": False,
                        "metacritic_score": 94,
                        "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring",
                        "positive_ratings": 460812,
                        "negative_ratings": 51238,
                        "achievements": 42,
                        "average_playtime": 5293,
                        "median_playtime": 4467,
                        "developers": ["FromSoftware Inc."],
                        "publishers": [
                            "Bandai Namco Entertainment",
                            "FromSoftware Inc.",
                        ],
                        "categories": [
                            "Single-player",
                            "Steam Achievements",
                            "Steam Trading Cards",
                            "Multi-player",
                            "Co-op",
                            "Full controller support",
                            "PvP",
                            "Online PvP",
                            "Online Co-op",
                        ],
                        "genres": ["RPG", "Action"],
                        "tags": [
                            "RPG",
                            "Difficult",
                            "Action",
                            "Third Person",
                            "Co-op",
                            "Singleplayer",
                            "Multiplayer",
                            "Open World",
                            "Great Soundtrack",
                            "Atmospheric",
                            "Violent",
                            "Action RPG",
                            "Fantasy",
                            "PvP",
                            "Online Co-Op",
                            "Walking Simulator",
                            "3D",
                            "Relaxing",
                            "Dark Fantasy",
                            "Souls-like",
                        ],
                    }
                },
                schema=GameSerializer(many=True),
            ),
            400: openapi.Response(
                description="Bad Request - Neither id nor name provided",
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )


"""
Swagger/OpenAPI schema decorator for game creation endpoint.

This decorator provides detailed schema information for the POST endpoint that creates a new game.
It specifies:
- HTTP method: POST
- Request body: Complete game details including
    - Basic info (name, release date, price)
    - Statistics (owners, peak users, playtime)
    - Content details (age rating, DLC count, description) 
    - Platform support (Windows, Mac, Linux)
    - Languages (interface and audio)
    - Media (header image)
    - External links (website, support)
    - Ratings (Metacritic, user ratings)
    - Related entities (developers, publishers, genres, tags)
- Response formats:
    - 201: Successfully created game with complete details
    - 400: Invalid request data

Returns:
    swagger_auto_schema: Decorator with complete schema definition for game creation
"""


def create_game_schema():
    return swagger_auto_schema(
        method="post",
        operation_description="Create a new game.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Elden Ring: Shadow of the Erdtree",
                ),
                "release_date": openapi.Schema(
                    type=openapi.TYPE_STRING, format="date", example="2024-06-12"
                ),
                "estimated_owners": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=20000000
                ),
                "peak_concurrent_users": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=781261
                ),
                "required_age": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=16, minimum=0, maximum=100
                ),
                "price": openapi.Schema(
                    type=openapi.TYPE_NUMBER, format="decimal", example=39.99, minimum=0
                ),
                "dlc_count": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=0, minimum=0
                ),
                "about_the_game": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="The ELDEN RING Shadow of the Erdtree expansion features an all-new story set in the Land of Shadow imbued with mystery, perilous dungeons, and new enemies, weapons and equipment.",
                    nullable=True,
                ),
                "supported_languages": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["English", "French", "Italian"],
                ),
                "full_audio_languages": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["English"],
                ),
                "header_image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="uri",
                    example="https://cdn.akamai.steamstatic.com/steam/apps/2778580/header.jpg",
                    nullable=True,
                ),
                "website": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="uri",
                    example="https://www.eldenring.jp/",
                    nullable=True,
                ),
                "support_url": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="uri",
                    example="https://www.bandainamcoent.com/support",
                    nullable=True,
                ),
                "support_email": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="email",
                    example="support@bandainamco.com",
                    nullable=True,
                ),
                "windows": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
                "mac": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
                "linux": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
                "metacritic_score": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    example=92,
                    minimum=0,
                    maximum=100,
                    nullable=True,
                ),
                "metacritic_url": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="uri",
                    example="https://www.metacritic.com/game/elden-ring-shadow-of-the-erdtree",
                    nullable=True,
                ),
                "positive_ratings": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=70501, minimum=0, nullable=True
                ),
                "negative_ratings": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=29821, minimum=0, nullable=True
                ),
                "achievements": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=0, minimum=0, nullable=True
                ),
                "average_playtime": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=5293, minimum=0
                ),
                "median_playtime": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=4467, minimum=0
                ),
                "developers": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["FromSoftware Inc."],
                ),
                "publishers": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["Bandai Namco Entertainment"],
                ),
                "categories": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["Single-player", "Multi-player", "PvP"],
                ),
                "genres": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["Action", "RPG"],
                ),
                "tags": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["Action", "RPG", "Souls-like"],
                ),
            },
        ),
        responses={
            201: openapi.Response(
                description="Game created successfully",
                examples={
                    "application/json": {
                        "message": "Game created successfully",
                        "game": {
                            "name": "Elden Ring: Shadow of the Erdtree",
                            "release_date": "2024-06-12",
                            "estimated_owners": 20000000,
                            "peak_concurrent_users": 781261,
                            "required_age": 16,
                            "price": 39.99,
                            "dlc_count": 0,
                            "about_the_game": "The ELDEN RING Shadow of the Erdtree expansion features an all-new story set in the Land of Shadow imbued with mystery, perilous dungeons, and new enemies, weapons and equipment.",
                            "supported_languages": ["English", "French", "Italian"],
                            "full_audio_languages": ["English"],
                            "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/2778580/header.jpg",
                            "website": "https://www.eldenring.jp/",
                            "support_url": "https://www.bandainamcoent.com/support",
                            "support_email": "support@bandainamco.com",
                            "windows": True,
                            "mac": False,
                            "linux": False,
                            "metacritic_score": 92,
                            "metacritic_url": "https://www.metacritic.com/game/elden-ring-shadow-of-the-erdtree",
                            "positive_ratings": 70501,
                            "negative_ratings": 29821,
                            "achievements": 0,
                            "average_playtime": 5293,
                            "median_playtime": 4467,
                            "developers": ["FromSoftware Inc."],
                            "publishers": ["Bandai Namco Entertainment"],
                            "categories": ["Single-player", "Multi-player", "PvP"],
                            "genres": ["Action", "RPG"],
                            "tags": ["Action", "RPG", "Souls-like"],
                        },
                    }
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="Game created successfully",
                        ),
                        "game": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "name": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="Elden Ring: Shadow of the Erdtree",
                                ),
                                "release_date": openapi.Schema(
                                    type=openapi.TYPE_STRING, example="2024-06-12"
                                ),
                                "estimated_owners": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=20000000
                                ),
                                "peak_concurrent_users": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=781261
                                ),
                                "required_age": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=16
                                ),
                                "price": openapi.Schema(
                                    type=openapi.TYPE_NUMBER, example=39.99
                                ),
                                "dlc_count": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=0
                                ),
                                "about_the_game": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="The ELDEN RING Shadow of the Erdtree expansion features an all-new story set in the Land of Shadow imbued with mystery, perilous dungeons, and new enemies, weapons and equipment.",
                                ),
                                "supported_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["English", "French", "Italian"],
                                ),
                                "full_audio_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["English"],
                                ),
                                "header_image": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="https://cdn.akamai.steamstatic.com/steam/apps/2778580/header.jpg",
                                ),
                                "website": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="https://www.eldenring.jp/",
                                ),
                                "support_url": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="https://www.bandainamcoent.com/support",
                                ),
                                "support_email": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="support@bandainamco.com",
                                ),
                                "windows": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN, example=True
                                ),
                                "mac": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN, example=False
                                ),
                                "linux": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN, example=False
                                ),
                                "metacritic_score": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=92
                                ),
                                "metacritic_url": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    example="https://www.metacritic.com/game/pc/elden-ring-shadow-of-the-erdtree",
                                ),
                                "positive_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=70501
                                ),
                                "negative_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=29821
                                ),
                                "achievements": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=0
                                ),
                                "average_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=5293
                                ),
                                "median_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=4467
                                ),
                                "developers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["FromSoftware Inc."],
                                ),
                                "publishers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["Bandai Namco Entertainment"],
                                ),
                                "categories": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["Single-player", "Multi-player", "PvP"],
                                ),
                                "genres": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["Action", "RPG"],
                                ),
                                "tags": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                    example=["Action", "RPG", "Souls-like"],
                                ),
                            },
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                description="Invalid request data",
            ),
        },
    )


"""
Returns a swagger_auto_schema decorator for the game update endpoint.

This schema defines the OpenAPI/Swagger documentation for the PATCH endpoint that updates an existing game.
It specifies:
- HTTP method: PATCH
- Query parameters:
    - id (optional): Integer ID of the game to update
    - name (optional): String name of the game to update
- Request body: Fields that can be updated, including:
    - Basic info (name, release date, price)
    - Statistics (owners, peak users, playtime)
    - Content details (age rating, DLC count, description)
    - Platform support (Windows, Mac, Linux)
    - Languages (interface and audio)
    - Media (header image)
    - External links (website, support)
    - Ratings (Metacritic, user ratings)
    - Related entities (developers, publishers, genres, tags)
- Response formats:
    - 200: Successfully updated game with complete details
    - 400: Invalid request data
    - 404: Game not found

Returns:
    swagger_auto_schema: Decorator with complete schema definition for game updates
"""


def update_game_schema():
    return swagger_auto_schema(
        methods=["patch"],
        operation_description="Update an existing game by ID or name",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="The unique identifier of the game to update",
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="The name of the game to update",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "website": openapi.Schema(
                    type=openapi.TYPE_STRING, example="https://www.eldenring.jp/"
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Game updated successfully",
                examples={
                    "application/json": {
                        "message": "Game updated successfully",
                        "game": {
                            "application/json": {
                                "id": 5504,
                                "name": "ELDEN RING",
                                "release_date": "2022-02-24",
                                "estimated_owners": 50000000,
                                "peak_concurrent_users": 46431,
                                "required_age": 16,
                                "price": "59.99",
                                "dlc_count": 0,
                                "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                                "supported_languages": [
                                    "English",
                                    "French",
                                    "German",
                                    "Polish",
                                    "Russian",
                                    "Italian",
                                    "Japanese",
                                    "Spanish - Spain",
                                    "Korean",
                                    "Portuguese - Brazil",
                                    "Simplified Chinese",
                                    "Traditional Chinese",
                                    "Spanish - Latin America",
                                    "Thai",
                                ],
                                "full_audio_languages": [
                                    "English",
                                    "Traditional Chinese",
                                ],
                                "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg",
                                "website": "https://www.eldenring.jp/",
                                "support_url": "https://www.bandainamcoent.com/support",
                                "support_email": "",
                                "windows": True,
                                "mac": False,
                                "linux": False,
                                "metacritic_score": 94,
                                "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring",
                                "positive_ratings": 460812,
                                "negative_ratings": 51238,
                                "achievements": 42,
                                "average_playtime": 5293,
                                "median_playtime": 4467,
                                "developers": ["FromSoftware Inc."],
                                "publishers": [
                                    "Bandai Namco Entertainment",
                                    "FromSoftware Inc.",
                                ],
                                "categories": [
                                    "Single-player",
                                    "Steam Achievements",
                                    "Steam Trading Cards",
                                    "Multi-player",
                                    "Co-op",
                                    "Full controller support",
                                    "PvP",
                                    "Online PvP",
                                    "Online Co-op",
                                ],
                                "genres": ["RPG", "Action"],
                                "tags": [
                                    "RPG",
                                    "Difficult",
                                    "Action",
                                    "Third Person",
                                    "Co-op",
                                    "Singleplayer",
                                    "Multiplayer",
                                    "Open World",
                                    "Great Soundtrack",
                                    "Atmospheric",
                                    "Violent",
                                    "Action RPG",
                                    "Fantasy",
                                    "PvP",
                                    "Online Co-Op",
                                    "Walking Simulator",
                                    "3D",
                                    "Relaxing",
                                    "Dark Fantasy",
                                    "Souls-like",
                                ],
                            }
                        },
                    }
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "game": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "name": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "release_date": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "estimated_owners": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "peak_concurrent_users": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "required_age": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "price": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "dlc_count": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "about_the_game": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "supported_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "full_audio_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "header_image": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "website": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "support_url": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "support_email": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "windows": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                ),
                                "mac": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                ),
                                "linux": openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                ),
                                "metacritic_score": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "metacritic_url": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "positive_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "negative_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "achievements": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "average_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "median_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                ),
                                "developers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "publishers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "categories": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "genres": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "tags": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                            },
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                description="Invalid request data",
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )


"""Swagger/OpenAPI schema for the DELETE game endpoint.

This schema documents the API endpoint that deletes a single game by ID or name.
It specifies:
- HTTP method: DELETE 
- Query parameters:
    - id (optional): Integer ID of the game to delete
    - name (optional): String name of the game to delete
- Response formats:
    - 204: Successfully deleted game with confirmation message
    - 404: Error when game not found
    - 400: Error when neither id nor name provided

Returns:
    swagger_auto_schema: Decorator configured with complete endpoint documentation
"""


def delete_game_schema():
    return swagger_auto_schema(
        method="delete",
        operation_description="Delete a game by ID or name.",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="The unique identifier of the game to delete",
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="The name of the game to delete",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        responses={
            204: openapi.Response(
                description="Game deleted successfully",
                examples={
                    "application/json": {
                        "message": "Game deleted successfully",
                    }
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: openapi.Response(
                description="Bad Request - Neither id nor name provided",
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )


"""
Swagger/OpenAPI schema for the GET /games endpoint.

This schema defines the API documentation for retrieving a paginated list of games,
with support for filtering and sorting options.

Query Parameters:
    filterBy (str, optional): Filter games by:
        - genre: Comma-separated list of genres (e.g. Action,RPG)
        - platform: Comma-separated list of platforms (e.g. windows,mac,linux)
        - year: Comma-separated list of years (e.g. 2021,2022,2023)
    sortBy (str, optional): Sort results by one of:
        - metacriticScore: Sort by Metacritic review score
        - price: Sort by game price
        - releaseDate: Sort by release date
    sortOrder (str, optional): Sort direction:
        - asc: Ascending order
        - desc: Descending order (default)
    page (int, optional): Page number for pagination results
    pageSize (int, optional): Number of results per page (default: 100, max: 100)

Returns:
    swagger_auto_schema: OpenAPI schema configuration with:
        - Method: GET
        - Parameters: filterBy, sortBy, sortOrder, page, pageSize
        - Responses:
            200: Successful response with paginated game results including:
                - Pagination metadata (count, next/previous page links)
                - Game details (basic info, stats, platforms, ratings, etc.)
            400: Bad request error for invalid parameter values
"""


def get_games_schema():
    return swagger_auto_schema(
        method="get",
        operation_description="Get a paginated list of games with optional filtering and sorting.",
        manual_parameters=[
            openapi.Parameter(
                "filterBy",
                openapi.IN_QUERY,
                description="Filter games by 'genre(Action,RPG)', 'platform(windows,mac,linux)', or 'year(2021,2022,2023)'",
                type=openapi.TYPE_STRING,
                required=False,
            ),
            openapi.Parameter(
                "sortBy",
                openapi.IN_QUERY,
                description="Sort by 'metacriticScore', 'price', or 'releaseDate'",
                type=openapi.TYPE_STRING,
                required=False,
            ),
            openapi.Parameter(
                "sortOrder",
                openapi.IN_QUERY,
                description="Sort direction: 'asc' or 'desc'",
                type=openapi.TYPE_STRING,
                required=False,
                default="desc",
            ),
            openapi.Parameter(
                "page",
                openapi.IN_QUERY,
                description="Page number",
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
            openapi.Parameter(
                "pageSize",
                openapi.IN_QUERY,
                description="Number of results per page (max 100)",
                type=openapi.TYPE_INTEGER,
                required=False,
                default=100,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": [
                        {
                            "count": 10,
                            "next": None,
                            "previous": None,
                            "results": [
                                {
                                    "id": 5504,
                                    "name": "ELDEN RING",
                                    "release_date": "2022-02-24",
                                    "estimated_owners": 50000000,
                                    "peak_concurrent_users": 46431,
                                    "required_age": 16,
                                    "price": "59.99",
                                    "dlc_count": 0,
                                    "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                                    "supported_languages": [
                                        "English",
                                        "French",
                                        "German",
                                        "Polish",
                                        "Russian",
                                        "Italian",
                                        "Japanese",
                                        "Spanish - Spain",
                                        "Korean",
                                        "Portuguese - Brazil",
                                        "Simplified Chinese",
                                        "Traditional Chinese",
                                        "Spanish - Latin America",
                                        "Thai",
                                    ],
                                    "full_audio_languages": [
                                        "English",
                                        "Traditional Chinese",
                                    ],
                                    "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg",
                                    "website": "https://www.eldenring.jp/",
                                    "support_url": "https://www.bandainamcoent.com/support",
                                    "support_email": "",
                                    "windows": True,
                                    "mac": False,
                                    "linux": False,
                                    "metacritic_score": 94,
                                    "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring",
                                    "positive_ratings": 460812,
                                    "negative_ratings": 51238,
                                    "achievements": 42,
                                    "average_playtime": 5293,
                                    "median_playtime": 4467,
                                    "developers": ["FromSoftware Inc."],
                                    "publishers": [
                                        "Bandai Namco Entertainment",
                                        "FromSoftware Inc.",
                                    ],
                                    "categories": [
                                        "Single-player",
                                        "Steam Achievements",
                                        "Steam Trading Cards",
                                        "Multi-player",
                                        "Co-op",
                                        "Full controller support",
                                        "PvP",
                                        "Online PvP",
                                        "Online Co-op",
                                    ],
                                    "genres": ["RPG", "Action"],
                                    "tags": [
                                        "RPG",
                                        "Difficult",
                                        "Action",
                                        "Third Person",
                                        "Co-op",
                                        "Singleplayer",
                                        "Multiplayer",
                                        "Open World",
                                        "Great Soundtrack",
                                        "Atmospheric",
                                        "Violent",
                                        "Action RPG",
                                        "Fantasy",
                                        "PvP",
                                        "Online Co-Op",
                                        "Walking Simulator",
                                        "3D",
                                        "Relaxing",
                                        "Dark Fantasy",
                                        "Souls-like",
                                    ],
                                }
                            ],
                        }
                    ]
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "count": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                        ),
                        "next": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "previous": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "results": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "name": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "release_date": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "estimated_owners": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "peak_concurrent_users": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "required_age": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "price": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "dlc_count": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "about_the_game": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "supported_languages": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "full_audio_languages": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "header_image": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "website": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "support_url": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "support_email": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "windows": openapi.Schema(
                                        type=openapi.TYPE_BOOLEAN,
                                    ),
                                    "mac": openapi.Schema(
                                        type=openapi.TYPE_BOOLEAN,
                                    ),
                                    "linux": openapi.Schema(
                                        type=openapi.TYPE_BOOLEAN,
                                    ),
                                    "metacritic_score": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "metacritic_url": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                    ),
                                    "positive_ratings": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "negative_ratings": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "achievements": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "average_playtime": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "median_playtime": openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                    ),
                                    "developers": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "publishers": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "categories": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "genres": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                    "tags": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                    ),
                                },
                            ),
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                description="Bad Request - Invalid parameter values provided",
            ),
        },
    )


"""
Swagger schema for the get_recommended_games endpoint.

This endpoint returns 5 recommended games based on a reference game that can be specified
either by ID or name. The recommendations are based on similarity in genres, tags, and other
game attributes.

Parameters:
    - id (int, optional): The unique identifier of the reference game
    - name (str, optional): The name of the reference game to search for

Returns:
    swagger_auto_schema: A decorated schema containing:
        - GET method specification
        - Operation description
        - Query parameters (id or name)
        - Response schemas:
            - 200: Successful response with:
                - reference_game: Full details of the requested game
                - recommended_games: Array of up to 5 similar games with their details
            - 400: Bad request when neither id nor name is provided
            - 404: Game not found error

Note:
    Either id or name must be provided, but not both. The recommendations are generated
    using a similarity algorithm that considers multiple game attributes including genres,
    tags, ratings, and player statistics to find the most relevant suggestions.
"""


def get_recommended_games_schema():
    return swagger_auto_schema(
        method="get",
        operation_description="Get 5 recommended games based on a reference game by ID or name.",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="The unique identifier of the reference game",
                type=openapi.TYPE_INTEGER,
                required=False,
            ),
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="The name of the reference game to search for",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": {
                        "reference_game": {
                            "id": 5504,
                            "name": "ELDEN RING",
                            "release_date": "2022-02-24",
                            "estimated_owners": 50000000,
                            "peak_concurrent_users": 46431,
                            "required_age": 16,
                            "price": "59.99",
                            "dlc_count": 0,
                            "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                            "supported_languages": [
                                "English",
                                "French",
                                "German",
                                "Polish",
                                "Russian",
                                "Italian",
                                "Japanese",
                                "Spanish - Spain",
                                "Korean",
                                "Portuguese - Brazil",
                                "Simplified Chinese",
                                "Traditional Chinese",
                                "Spanish - Latin America",
                                "Thai",
                            ],
                            "full_audio_languages": [
                                "English",
                                "Traditional Chinese",
                            ],
                            "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg",
                            "website": "https://www.eldenring.jp/",
                            "support_url": "https://www.bandainamcoent.com/support",
                            "support_email": "",
                            "windows": True,
                            "mac": False,
                            "linux": False,
                            "metacritic_score": 94,
                            "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring",
                            "positive_ratings": 460812,
                            "negative_ratings": 51238,
                            "achievements": 42,
                            "average_playtime": 5293,
                            "median_playtime": 4467,
                            "developers": ["FromSoftware Inc."],
                            "publishers": [
                                "Bandai Namco Entertainment",
                                "FromSoftware Inc.",
                            ],
                            "categories": [
                                "Single-player",
                                "Steam Achievements",
                                "Steam Trading Cards",
                                "Multi-player",
                                "Co-op",
                                "Full controller support",
                                "PvP",
                                "Online PvP",
                                "Online Co-op",
                            ],
                            "genres": ["RPG", "Action"],
                            "tags": [
                                "RPG",
                                "Difficult",
                                "Action",
                                "Third Person",
                                "Co-op",
                                "Singleplayer",
                                "Multiplayer",
                                "Open World",
                                "Great Soundtrack",
                                "Atmospheric",
                                "Violent",
                                "Action RPG",
                                "Fantasy",
                                "PvP",
                                "Online Co-Op",
                                "Walking Simulator",
                                "3D",
                                "Relaxing",
                                "Dark Fantasy",
                                "Souls-like",
                            ],
                        },
                        "recommended_games": [
                            {
                                "id": 3301,
                                "name": "Nioh: Complete Edition",
                                "release_date": "2017-11-07",
                                "estimated_owners": "1000000 - 2000000",
                                "peak_ccu": 463,
                                "required_age": 17,
                                "price": "49.99",
                                "dlc_count": 0,
                                "about_the_game": "Ready to die? Experience the newest brutal action game from Team NINJA and Koei Tecmo Games. In the age of samurai, a lone traveler lands on the shores of Japan. He must fight his way through the vicious warriors and supernatural Yokai that infest the land in order to find that which he seeks. The Complete Edition contains the full game, as well as the three expansions with additional story chapters: Dragon of the North, Defiant Honor, and Bloodshed's End. Dragon of the North This expansion opens up the Tohoku region, where the 'one-eyed dragon' Date Masamune is secretly gathering spirit stones. Defiant Honor Fight your way through the Siege of Osaka's winter campaign as you follow the story of one of Japan's greatest generals from the Warring States period, the brave Sanada Yukimura. Bloodshed's End Join the summer campaign of the Siege of Osaka as the Warring States period draws to a close in this, the final chapter of William's tale. Steam Exclusive Bonus Enjoy wearing the 'Dharmachakra Kabuto,' a helmet exclusive to the Steam version of Nioh! You can claim yours by selecting 'Boons' from a shrine.",
                                "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Traditional Chinese']",
                                "full_audio_languages": "['English', 'Japanese', 'Traditional Chinese']",
                                "reviews": "",
                                "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/485510/header.jpg?t=1655226032",
                                "website": "http://teamninja-studio.com/nioh/lang/",
                                "support_url": "https://koeitecmo.info/inquiry/kta/",
                                "support_email": "",
                                "windows": True,
                                "mac": False,
                                "linux": False,
                                "metacritic_score": 84,
                                "metacritic_url": "https://www.metacritic.com/game/pc/nioh-complete-edition?ftag=MCD-06-10aaa1f",
                                "user_score": 0,
                                "positive": 23944,
                                "negative": 5778,
                                "achievements": 79,
                                "recommendations": 22411,
                                "notes": "",
                                "average_playtime_forever": 2847,
                                "average_playtime_two_weeks": 879,
                                "median_playtime_forever": 989,
                                "median_playtime_two_weeks": 879,
                                "developers": "KOEI TECMO GAMES CO., LTD.",
                                "publishers": "KOEI TECMO GAMES CO., LTD.",
                                "categories": "Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards,Steam Cloud,Stats,Steam Leaderboards",
                                "genres": "Action,RPG",
                                "tags": "Souls-like,Action,RPG,Difficult,Hack and Slash,Dark Fantasy,Ninja,Action RPG,Third Person,JRPG,Singleplayer,Co-op,Multiplayer,Historical,Loot,Fantasy,Adventure,Atmospheric,Nudity,Great Soundtrack",
                                "screenshots": "https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_744edaca2857bdb6cfae5eddddf38b01456b27d6.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_a3e52866214ca618474a13372c092ae42d922069.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_658b41c5cd7a701d2946cbbc9ede13592d0adc31.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_75f7f116b8b846f8e094cfcae680e648798c51ef.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_d211be4ecfb2ec61fcd1b3bee44797d00828a8ac.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_23a6fbc39ff1adaab44553bf8df74f1264933d10.1920x1080.jpg?t=1655226032,https://cdn.akamai.steamstatic.com/steam/apps/485510/ss_ed60bda68330839c4995d852dfa32d3f56cc2f21.1920x1080.jpg?t=1655226032",
                                "movies": "http://cdn.akamai.steamstatic.com/steam/apps/256700241/movie_max.mp4?t=1509956268,http://cdn.akamai.steamstatic.com/steam/apps/256696529/movie_max.mp4?t=1507025887",
                            },
                        ],
                    }
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "reference_game": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=5504
                                ),
                                "name": openapi.Schema(
                                    type=openapi.TYPE_STRING, example="ELDEN RING"
                                ),
                                "release_date": openapi.Schema(
                                    type=openapi.TYPE_STRING, example="2022-02-24"
                                ),
                                "estimated_owners": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=50000000
                                ),
                                "peak_concurrent_users": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=46431
                                ),
                                "required_age": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=16
                                ),
                                "price": openapi.Schema(
                                    type=openapi.TYPE_STRING, example="59.99"
                                ),
                                "dlc_count": openapi.Schema(
                                    type=openapi.TYPE_INTEGER, example=0
                                ),
                                "about_the_game": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                "supported_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "full_audio_languages": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "header_image": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                "website": openapi.Schema(type=openapi.TYPE_STRING),
                                "support_url": openapi.Schema(type=openapi.TYPE_STRING),
                                "support_email": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                "windows": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                "mac": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                "linux": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                "metacritic_score": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "metacritic_url": openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                "positive_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "negative_ratings": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "achievements": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "average_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "median_playtime": openapi.Schema(
                                    type=openapi.TYPE_INTEGER
                                ),
                                "developers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "publishers": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "categories": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "genres": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                                "tags": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(type=openapi.TYPE_STRING),
                                ),
                            },
                        ),
                        "recommended_games": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                    "release_date": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "estimated_owners": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "peak_ccu": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "required_age": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "price": openapi.Schema(type=openapi.TYPE_STRING),
                                    "dlc_count": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "about_the_game": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "supported_languages": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "full_audio_languages": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "reviews": openapi.Schema(type=openapi.TYPE_STRING),
                                    "header_image": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "website": openapi.Schema(type=openapi.TYPE_STRING),
                                    "support_url": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "support_email": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "windows": openapi.Schema(
                                        type=openapi.TYPE_BOOLEAN
                                    ),
                                    "mac": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                    "linux": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                    "metacritic_score": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "metacritic_url": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "user_score": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "positive": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "negative": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "achievements": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "recommendations": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "notes": openapi.Schema(type=openapi.TYPE_STRING),
                                    "average_playtime_forever": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "average_playtime_two_weeks": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "median_playtime_forever": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "median_playtime_two_weeks": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "developers": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "publishers": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "categories": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "genres": openapi.Schema(type=openapi.TYPE_STRING),
                                    "tags": openapi.Schema(type=openapi.TYPE_STRING),
                                    "screenshots": openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    "movies": openapi.Schema(type=openapi.TYPE_STRING),
                                },
                            ),
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                description="Bad Request - Neither id nor name provided",
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )
