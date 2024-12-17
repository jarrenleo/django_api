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
    - 200: Successful response with full game details
    - 400: Error when neither id nor name provided
    - 404: Error when game not found

The successful response includes a complete game object with all fields like name,
release date, pricing, descriptions, statistics, etc.

Returns:
    swagger_auto_schema decorator configured with the endpoint documentation
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
                        "id": 1979,
                        "name": "ELDEN RING",
                        "release_date": "2022-02-24",
                        "estimated_owners": "20000000 - 50000000",
                        "peak_ccu": 46431,
                        "required_age": 16,
                        "price": "59.99",
                        "dlc_count": 0,
                        "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                        "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Thai', 'Traditional Chinese']",
                        "full_audio_languages": "['English', 'Traditional Chinese']",
                        "reviews": "“Put a ring on it.” 10/10 – IGN “An unmissable open-world masterpiece.” 10/10 – Gaming Bible “Exploration is jaw dropping.” 5/5 – Games Radar",
                        "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1654259241",
                        "website": "",
                        "support_url": "https://www.bandainamcoent.com/support",
                        "support_email": "",
                        "windows": True,
                        "mac": False,
                        "linux": False,
                        "metacritic_score": 94,
                        "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring?ftag=MCD-06-10aaa1f",
                        "user_score": 0,
                        "positive": 460812,
                        "negative": 51238,
                        "achievements": 42,
                        "recommendations": 391693,
                        "notes": "",
                        "average_playtime_forever": 5293,
                        "average_playtime_two_weeks": 403,
                        "median_playtime_forever": 4467,
                        "median_playtime_two_weeks": 131,
                        "developers": "FromSoftware Inc.",
                        "publishers": "FromSoftware Inc.,Bandai Namco Entertainment",
                        "categories": "Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards",
                        "genres": "Action,RPG",
                        "tags": "Souls-like,Relaxing,Dark Fantasy,RPG,Difficult,Open World,Action RPG,Third Person,Fantasy,Multiplayer,Online Co-Op,Singleplayer,Action,Co-op,PvP,Violent,Atmospheric,3D,Great Soundtrack,Walking Simulator",
                        "screenshots": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e80a907c2c43337e53316c71555c3c3035a1343e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_25cd489871907387c1b915022a96b196661b6e17.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3e556415d1bda00d749b2166ced264bec76f06ee.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ae44317e3bd07b7690b4d62cc5d0d1df30367a91.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_c372274833ae6e5437b952fa1979430546a43ad9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e87a3e84890ab19f8995566e62762d5f8ed39315.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3aec1455923ef49f4e777c2a94dbcd0256f77eb0.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_b87601dee58f4dbc36e40a8d803dc6a53ceefe07.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_8b58d96262fb0d62a482621b86c6ff85f4f57997.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_1011610a0e330c41a75ffd0b3a9a1bac3205c46a.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_41e2e8f3b0ad631e929e0c2ec3d1f21de883e98c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7dcd7e6c42024c2d5a5a31d758039ded13a47527.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_abd681cde3402155a35edb82919b7602cc7ec338.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_0b6e59057b02392b21dde62b4dde65d447e1fa3c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7523a8fc7775ae65cabd94d092ebecbd963258b6.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_a176eea67cd421307a6c627514129237d6202890.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ebb332e63dfab864c3bf3c3b1001b69f4da25f9f.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_24bd769aeffacd45fcd3a7ae9efde22b24b5fca9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_75f25974c20b8704fe5ee246f74896b550088d3e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_fb2957cce97f4633bc743b561f76865e6993c781.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_35ff7ed4b67e2bb73e54f6c10a4f8d9390c16203.1920x1080.jpg?t=1654259241",
                        "movies": "http://cdn.akamai.steamstatic.com/steam/apps/256889452/movie_max.mp4?t=1654109247,http://cdn.akamai.steamstatic.com/steam/apps/256875477/movie_max.mp4?t=1645743469,http://cdn.akamai.steamstatic.com/steam/apps/256864891/movie_max.mp4?t=1645830855,http://cdn.akamai.steamstatic.com/steam/apps/256859890/movie_max.mp4?t=1641845061,http://cdn.akamai.steamstatic.com/steam/apps/256839312/movie_max.mp4?t=1641422486",
                    }
                },
                schema=GameSerializer(),
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
            - genre (e.g. Action,RPG)
            - platform (e.g. windows,mac,linux)
            - year (e.g. 2021,2022,2023)
        sortBy (str, optional): Sort results by one of:
            - metacriticScore
            - price
            - releaseDate
        sortOrder (str, optional): Sort direction, either 'asc' or 'desc'. Defaults to 'desc'
        page (int, optional): Page number for pagination
        pageSize (int, optional): Number of results per page, max 100. Defaults to 100

    Returns:
        swagger_auto_schema: OpenAPI schema configuration with:
            - Method: GET
            - Parameters: filterBy, sortBy, sortOrder, page, pageSize
            - Responses:
                200: Successful response with paginated game results
                400: Bad request error
    """


def get_games_schema():
    return swagger_auto_schema(
        method="get",
        operation_description="Get a paginated list of games with optional filtering and sorting.",
        manual_parameters=[
            openapi.Parameter(
                "filterBy",
                openapi.IN_QUERY,
                description="Filter games by genre(Action,RPG), platform(windows,mac,linux), or year(2021,2022,2023)",
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
                                    "id": 3771,
                                    "name": "Hogwarts Legacy",
                                    "release_date": "2023-02-10",
                                    "estimated_owners": "5000000 - 10000000",
                                    "peak_ccu": 872138,
                                    "required_age": 0,
                                    "price": "59.99",
                                    "dlc_count": 1,
                                    "about_the_game": "Hogwarts Legacy is an open-world action RPG set in the world first introduced in the Harry Potter books. Embark on a journey through familiar and new locations as you explore and discover magical beasts, customize your character and craft potions, master spell casting, upgrade talents and become the wizard you want to be. Experience Hogwarts in the 1800s. Your character is a student who holds the key to an ancient secret that threatens to tear the wizarding world apart. Make allies, battle Dark wizards, and ultimately decide the fate of the wizarding world. Your legacy is what you make of it. Live the Unwritten.",
                                    "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Arabic', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Traditional Chinese']",
                                    "full_audio_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Portuguese - Brazil', 'Spanish - Latin America', 'Traditional Chinese']",
                                    "reviews": "",
                                    "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/990080/header.jpg?t=1676056674",
                                    "website": "https://www.hogwartslegacy.com/",
                                    "support_url": "https://portkeygamessupport.wbgames.com/hc",
                                    "support_email": "support@wbgames.com",
                                    "windows": True,
                                    "mac": False,
                                    "linux": False,
                                    "metacritic_score": 84,
                                    "metacritic_url": "https://www.metacritic.com/game/pc/hogwarts-legacy?ftag=MCD-06-10aaa1f",
                                    "user_score": 0,
                                    "positive": 33521,
                                    "negative": 2000,
                                    "achievements": 45,
                                    "recommendations": 55658,
                                    "notes": "",
                                    "average_playtime_forever": 661,
                                    "average_playtime_two_weeks": 661,
                                    "median_playtime_forever": 501,
                                    "median_playtime_two_weeks": 501,
                                    "developers": "Avalanche Software",
                                    "publishers": "Warner Bros. Games",
                                    "categories": "Single-player,Steam Achievements,Full controller support,In-App Purchases,Steam Cloud",
                                    "genres": "Action,Adventure,RPG",
                                    "tags": "Magic,Fantasy,Open World,Adventure,Singleplayer,RPG,Character Customization,Exploration,Story Rich,Third Person,Action-Adventure,Atmospheric,Action RPG,Action,Combat,Choices Matter,Puzzle,Great Soundtrack,Dark,Family Friendly",
                                    "screenshots": "https://cdn.akamai.steamstatic.com/steam/apps/990080/ss_725bf58485beb4aa37a3a69c1e2baa69bf3e4653.1920x1080.jpg?t=1676056674,https://cdn.akamai.steamstatic.com/steam/apps/990080/ss_df93b5e8a183f7232d68be94ae78920a90de1443.1920x1080.jpg?t=1676056674,https://cdn.akamai.steamstatic.com/steam/apps/990080/ss_94058497bf0f8fabdde17ee8d59bece609a60663.1920x1080.jpg?t=1676056674,https://cdn.akamai.steamstatic.com/steam/apps/990080/ss_8e08976236d29b1897769257ac3c64e9264792a5.1920x1080.jpg?t=1676056674,https://cdn.akamai.steamstatic.com/steam/apps/990080/ss_d4930d675af053dc1e61a876a34fc003e85e261f.1920x1080.jpg?t=1676056674",
                                    "movies": "http://cdn.akamai.steamstatic.com/steam/apps/256926764/movie_max.mp4?t=1674596507,http://cdn.akamai.steamstatic.com/steam/apps/256926763/movie_max.mp4?t=1674596513",
                                },
                            ],
                        }
                    ]
                },
                schema=GameSerializer(),
            ),
            400: openapi.Response(
                description="Bad Request",
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
            - 200: Successful response with reference game and recommended games
            - 400: Bad request when neither id nor name is provided
            - 404: Game not found error

Note:
    Either id or name must be provided, but not both. The response includes both the
    reference game details and up to 5 recommended similar games.
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
                            "id": 1979,
                            "name": "ELDEN RING",
                            "release_date": "2022-02-24",
                            "estimated_owners": "20000000 - 50000000",
                            "peak_ccu": 46431,
                            "required_age": 16,
                            "price": "59.99",
                            "dlc_count": 0,
                            "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                            "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Thai', 'Traditional Chinese']",
                            "full_audio_languages": "['English', 'Traditional Chinese']",
                            "reviews": "“Put a ring on it.” 10/10 – IGN “An unmissable open-world masterpiece.” 10/10 – Gaming Bible “Exploration is jaw dropping.” 5/5 – Games Radar",
                            "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1654259241",
                            "website": "",
                            "support_url": "https://www.bandainamcoent.com/support",
                            "support_email": "",
                            "windows": True,
                            "mac": False,
                            "linux": False,
                            "metacritic_score": 94,
                            "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring?ftag=MCD-06-10aaa1f",
                            "user_score": 0,
                            "positive": 460812,
                            "negative": 51238,
                            "achievements": 42,
                            "recommendations": 391693,
                            "notes": "",
                            "average_playtime_forever": 5293,
                            "average_playtime_two_weeks": 403,
                            "median_playtime_forever": 4467,
                            "median_playtime_two_weeks": 131,
                            "developers": "FromSoftware Inc.",
                            "publishers": "FromSoftware Inc.,Bandai Namco Entertainment",
                            "categories": "Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards",
                            "genres": "Action,RPG",
                            "tags": "Souls-like,Relaxing,Dark Fantasy,RPG,Difficult,Open World,Action RPG,Third Person,Fantasy,Multiplayer,Online Co-Op,Singleplayer,Action,Co-op,PvP,Violent,Atmospheric,3D,Great Soundtrack,Walking Simulator",
                            "screenshots": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e80a907c2c43337e53316c71555c3c3035a1343e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_25cd489871907387c1b915022a96b196661b6e17.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3e556415d1bda00d749b2166ced264bec76f06ee.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ae44317e3bd07b7690b4d62cc5d0d1df30367a91.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_c372274833ae6e5437b952fa1979430546a43ad9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e87a3e84890ab19f8995566e62762d5f8ed39315.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3aec1455923ef49f4e777c2a94dbcd0256f77eb0.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_b87601dee58f4dbc36e40a8d803dc6a53ceefe07.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_8b58d96262fb0d62a482621b86c6ff85f4f57997.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_1011610a0e330c41a75ffd0b3a9a1bac3205c46a.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_41e2e8f3b0ad631e929e0c2ec3d1f21de883e98c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7dcd7e6c42024c2d5a5a31d758039ded13a47527.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_abd681cde3402155a35edb82919b7602cc7ec338.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_0b6e59057b02392b21dde62b4dde65d447e1fa3c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7523a8fc7775ae65cabd94d092ebecbd963258b6.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_a176eea67cd421307a6c627514129237d6202890.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ebb332e63dfab864c3bf3c3b1001b69f4da25f9f.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_24bd769aeffacd45fcd3a7ae9efde22b24b5fca9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_75f25974c20b8704fe5ee246f74896b550088d3e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_fb2957cce97f4633bc743b561f76865e6993c781.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_35ff7ed4b67e2bb73e54f6c10a4f8d9390c16203.1920x1080.jpg?t=1654259241",
                            "movies": "http://cdn.akamai.steamstatic.com/steam/apps/256889452/movie_max.mp4?t=1654109247,http://cdn.akamai.steamstatic.com/steam/apps/256875477/movie_max.mp4?t=1645743469,http://cdn.akamai.steamstatic.com/steam/apps/256864891/movie_max.mp4?t=1645830855,http://cdn.akamai.steamstatic.com/steam/apps/256859890/movie_max.mp4?t=1641845061,http://cdn.akamai.steamstatic.com/steam/apps/256839312/movie_max.mp4?t=1641422486",
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
                schema=GameSerializer(),
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
It specifies the expected request body structure and possible response scenarios.

Request Body:
    - name (str): Name of the game
    - release_date (date): Release date in YYYY-MM-DD format
    - estimated_owners (str): Estimated range of game owners
    - peak_ccu (int): Peak concurrent users
    - required_age (int): Required age to play
    - price (float): Game price
    - dlc_count (int): Number of DLCs
    - about_the_game (str): Game description
    - supported_languages (str): List of supported languages
    - full_audio_languages (str): List of languages with full audio support
    - reviews (str): Game reviews
    - header_image (str): URL of the game's header image
    - website (str): Game's official website
    - support_url (str): Support page URL
    - support_email (str): Support email address
    - windows/mac/linux (bool): Platform availability
    - metacritic_score (int): Metacritic rating
    - metacritic_url (str): Metacritic page URL
    - user_score (float): User rating
    - positive/negative (int): Number of positive/negative reviews
    - achievements (int): Number of achievements
    - recommendations (int): Number of recommendations
    - notes (str): Additional notes
    - average_playtime_forever/two_weeks (str): Average playtime statistics
    - median_playtime_forever/two_weeks (str): Median playtime statistics
    - developers (str): Game developers
    - publishers (str): Game publishers
    - categories (str): Game categories
    - genres (str): Game genres
    - tags (str): Game tags
    - screenshots (str): Screenshot URLs
    - movies (str): Movie/trailer URLs

Returns:
    swagger_auto_schema: Decorator with complete schema definition for game creation

Responses:
    201: Game created successfully
    400: Invalid request data
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
                    type=openapi.TYPE_STRING, example="20000000 - 50000000"
                ),
                "peak_ccu": openapi.Schema(type=openapi.TYPE_INTEGER, example=781261),
                "required_age": openapi.Schema(type=openapi.TYPE_INTEGER, example=16),
                "price": openapi.Schema(
                    type=openapi.TYPE_NUMBER, format="float", example=39.99
                ),
                "dlc_count": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                "about_the_game": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="The ELDEN RING Shadow of the Erdtree expansion features an all-new story set in the Land of Shadow imbued with mystery, perilous dungeons, and new enemies, weapons and equipment.",
                ),
                "supported_languages": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Thai', 'Traditional Chinese']",
                ),
                "full_audio_languages": openapi.Schema(
                    type=openapi.TYPE_STRING, example="['English']"
                ),
                "reviews": openapi.Schema(type=openapi.TYPE_STRING, example="-"),
                "header_image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1654259241",
                ),
                "website": openapi.Schema(
                    type=openapi.TYPE_STRING, example="https://eldenring.com/"
                ),
                "support_url": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="https://www.bandainamcoent.com/support",
                ),
                "support_email": openapi.Schema(
                    type=openapi.TYPE_STRING, example="bandainamcoent@support.com"
                ),
                "windows": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
                "mac": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
                "linux": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
                "metacritic_score": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example=92
                ),
                "metacritic_url": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="https://www.metacritic.com/game/pc/elden-ring-shadow-of-the-erdtree?ftag=MCD-06-10aaa1f",
                ),
                "user_score": openapi.Schema(
                    type=openapi.TYPE_NUMBER, format="float", example=70
                ),
                "positive": openapi.Schema(type=openapi.TYPE_INTEGER, example=70501),
                "negative": openapi.Schema(type=openapi.TYPE_INTEGER, example=29821),
                "achievements": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                "recommendations": openapi.Schema(
                    type=openapi.TYPE_INTEGER, example="-"
                ),
                "notes": openapi.Schema(type=openapi.TYPE_STRING, example="-"),
                "average_playtime_forever": openapi.Schema(
                    type=openapi.TYPE_STRING, example=5293
                ),
                "average_playtime_two_weeks": openapi.Schema(
                    type=openapi.TYPE_STRING, example=403
                ),
                "median_playtime_forever": openapi.Schema(
                    type=openapi.TYPE_STRING, example=4467
                ),
                "median_playtime_two_weeks": openapi.Schema(
                    type=openapi.TYPE_STRING, example=131
                ),
                "developers": openapi.Schema(
                    type=openapi.TYPE_STRING, example="FromSoftware, Inc."
                ),
                "publishers": openapi.Schema(
                    type=openapi.TYPE_STRING, example="Bandai Namco Entertainment"
                ),
                "categories": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards",
                ),
                "genres": openapi.Schema(
                    type=openapi.TYPE_STRING, example="Action,RPG"
                ),
                "tags": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    example="Action,RPG,Souls-like,Difficult,Fantasy",
                ),
                "screenshots": openapi.Schema(type=openapi.TYPE_STRING, example="-"),
                "movies": openapi.Schema(type=openapi.TYPE_STRING, example="-"),
            },
        ),
        responses={
            201: openapi.Response(
                description="Game created successfully",
                examples={
                    "application/json": {
                        "name": "Elden Ring: Shadow of the Erdtree",
                        "release_date": "2024-06-12",
                        "estimated_owners": "20000000 - 50000000",
                        "peak_ccu": 781261,
                        "required_age": 16,
                        "price": 39.99,
                        "dlc_count": 0,
                        "about_the_game": "The ELDEN RING Shadow of the Erdtree expansion features an all-new story set in the Land of Shadow imbued with mystery, perilous dungeons, and new enemies, weapons and equipment.",
                        "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Thai', 'Traditional Chinese']",
                        "full_audio_languages": "['English']",
                        "reviews": "-",
                        "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1654259241",
                        "website": "https://eldenring.com/",
                        "support_url": "https://www.bandainamcoent.com/support",
                        "support_email": "bandainamcoent@support.com",
                        "windows": True,
                        "mac": True,
                        "linux": True,
                        "metacritic_score": 92,
                        "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring-shadow-of-the-erdtree?ftag=MCD-06-10aaa1f",
                        "user_score": 70,
                        "positive": 70501,
                        "negative": 29821,
                        "achievements": 0,
                        "recommendations": 0,
                        "notes": "-",
                        "average_playtime_forever": "5293",
                        "average_playtime_two_weeks": "403",
                        "median_playtime_forever": "4467",
                        "median_playtime_two_weeks": "131",
                        "developers": "FromSoftware, Inc.",
                        "publishers": "Bandai Namco Entertainment",
                        "categories": "Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards",
                        "genres": "Action,RPG",
                        "tags": "Action,RPG,Souls-like,Difficult,Fantasy",
                        "screenshots": "-",
                        "movies": "-",
                    }
                },
                schema=GameSerializer(),
            ),
            400: openapi.Response(
                description="Invalid request data",
            ),
        },
    )


""""
Returns a swagger_auto_schema decorator for the game update endpoint.

This schema defines:
- PATCH method for updating games
- Query parameters for game identification (id or name)
- Request body specification for updatable fields
- Response specifications for success and error cases

Returns:
    swagger_auto_schema: A decorator that provides OpenAPI/Swagger documentation
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
                                "id": 1979,
                                "name": "ELDEN RING",
                                "release_date": "2022-02-24",
                                "estimated_owners": "20000000 - 50000000",
                                "peak_ccu": 46431,
                                "required_age": 16,
                                "price": "59.99",
                                "dlc_count": 0,
                                "about_the_game": "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between. • A Vast World Full of Excitement A vast world where open fields with a variety of situations and huge dungeons with complex and three-dimensional designs are seamlessly connected. As you explore, the joy of discovering unknown and overwhelming threats await you, leading to a high sense of accomplishment. • Create your Own Character In addition to customizing the appearance of your character, you can freely combine the weapons, armor, and magic that you equip. You can develop your character according to your play style, such as increasing your muscle strength to become a strong warrior, or mastering magic. • An Epic Drama Born from a Myth A multilayered story told in fragments. An epic drama in which the various thoughts of the characters intersect in the Lands Between. • Unique Online Play that Loosely Connects You to Others In addition to multiplayer, where you can directly connect with other players and travel together, the game supports a unique asynchronous online element that allows you to feel the presence of others.",
                                "supported_languages": "['English', 'French', 'Italian', 'German', 'Spanish - Spain', 'Japanese', 'Korean', 'Polish', 'Portuguese - Brazil', 'Russian', 'Simplified Chinese', 'Spanish - Latin America', 'Thai', 'Traditional Chinese']",
                                "full_audio_languages": "['English', 'Traditional Chinese']",
                                "reviews": "“Put a ring on it.” 10/10 – IGN “An unmissable open-world masterpiece.” 10/10 – Gaming Bible “Exploration is jaw dropping.” 5/5 – Games Radar",
                                "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1654259241",
                                "website": "https://www.eldenring.jp/",
                                "support_url": "https://www.bandainamcoent.com/support",
                                "support_email": "",
                                "windows": True,
                                "mac": False,
                                "linux": False,
                                "metacritic_score": 94,
                                "metacritic_url": "https://www.metacritic.com/game/pc/elden-ring?ftag=MCD-06-10aaa1f",
                                "user_score": 0,
                                "positive": 460812,
                                "negative": 51238,
                                "achievements": 42,
                                "recommendations": 391693,
                                "notes": "",
                                "average_playtime_forever": 5293,
                                "average_playtime_two_weeks": 403,
                                "median_playtime_forever": 4467,
                                "median_playtime_two_weeks": 131,
                                "developers": "FromSoftware Inc.",
                                "publishers": "FromSoftware Inc.,Bandai Namco Entertainment",
                                "categories": "Single-player,Multi-player,PvP,Online PvP,Co-op,Online Co-op,Steam Achievements,Full controller support,Steam Trading Cards",
                                "genres": "Action,RPG",
                                "tags": "Souls-like,Relaxing,Dark Fantasy,RPG,Difficult,Open World,Action RPG,Third Person,Fantasy,Multiplayer,Online Co-Op,Singleplayer,Action,Co-op,PvP,Violent,Atmospheric,3D,Great Soundtrack,Walking Simulator",
                                "screenshots": "https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e80a907c2c43337e53316c71555c3c3035a1343e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_25cd489871907387c1b915022a96b196661b6e17.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3e556415d1bda00d749b2166ced264bec76f06ee.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ae44317e3bd07b7690b4d62cc5d0d1df30367a91.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_c372274833ae6e5437b952fa1979430546a43ad9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_e87a3e84890ab19f8995566e62762d5f8ed39315.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_3aec1455923ef49f4e777c2a94dbcd0256f77eb0.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_b87601dee58f4dbc36e40a8d803dc6a53ceefe07.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_8b58d96262fb0d62a482621b86c6ff85f4f57997.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_1011610a0e330c41a75ffd0b3a9a1bac3205c46a.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_41e2e8f3b0ad631e929e0c2ec3d1f21de883e98c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7dcd7e6c42024c2d5a5a31d758039ded13a47527.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_abd681cde3402155a35edb82919b7602cc7ec338.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_0b6e59057b02392b21dde62b4dde65d447e1fa3c.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_7523a8fc7775ae65cabd94d092ebecbd963258b6.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_a176eea67cd421307a6c627514129237d6202890.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ebb332e63dfab864c3bf3c3b1001b69f4da25f9f.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_24bd769aeffacd45fcd3a7ae9efde22b24b5fca9.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_75f25974c20b8704fe5ee246f74896b550088d3e.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_fb2957cce97f4633bc743b561f76865e6993c781.1920x1080.jpg?t=1654259241,https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_35ff7ed4b67e2bb73e54f6c10a4f8d9390c16203.1920x1080.jpg?t=1654259241",
                                "movies": "http://cdn.akamai.steamstatic.com/steam/apps/256889452/movie_max.mp4?t=1654109247,http://cdn.akamai.steamstatic.com/steam/apps/256875477/movie_max.mp4?t=1645743469,http://cdn.akamai.steamstatic.com/steam/apps/256864891/movie_max.mp4?t=1645830855,http://cdn.akamai.steamstatic.com/steam/apps/256859890/movie_max.mp4?t=1641845061,http://cdn.akamai.steamstatic.com/steam/apps/256839312/movie_max.mp4?t=1641422486",
                            }
                        },
                    }
                },
                schema=GameSerializer(),
            ),
            400: openapi.Response(
                description="Invalid request data",
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )


"""Generate OpenAPI/Swagger documentation for the delete game endpoint.

This function creates a swagger_auto_schema decorator that documents the DELETE
endpoint for games. It specifies that games can be deleted either by their ID
or name via query parameters.

Parameters:
    None

Returns:
    swagger_auto_schema: A decorator containing the OpenAPI specification including:
        - DELETE method specification
        - Query parameters for game ID and name
        - Response specifications for success and error cases
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
            ),
            404: openapi.Response(
                description="Game not found",
            ),
        },
    )
