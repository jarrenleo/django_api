import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import (
    SupportedLanguage,
    FullAudioLanguage,
    Developer,
    Publisher,
    Category,
    Genre,
    Tag,
    Game,
)


class Command(BaseCommand):
    help = "Import games data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def parse_list(self, list_str):
        if not list_str:
            return []
        if list_str.startswith("[") and list_str.endswith("]"):
            list_str = list_str[1:-1]
            return [item.strip().strip("''") for item in list_str.split(",")]

        return [item.strip() for item in list_str.split(",")]

    def parse_boolean(self, boolean_str):
        if not boolean_str:
            return False
        return boolean_str.lower() == "true"

    def clean_date(self, date_str):
        try:
            release_date = datetime.strptime(date_str, "%b %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            release_date = datetime.strptime(date_str, "%b %Y").strftime("%Y-%m-1")
        return release_date

    def extract_estimated_owners(self, owners_str):
        if not owners_str or owners_str == "0 - 0":
            return 0
        try:
            return int(owners_str.split(" - ")[1].replace(",", ""))
        except (ValueError, IndexError):
            return 0

    def handle(self, *args, **kwargs):
        with open("data/data.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Create or get supported languages
                supported_languages = self.parse_list(row["Supported languages"])
                supported_languages_objects = []
                for language in supported_languages:
                    language_object, _ = SupportedLanguage.objects.get_or_create(
                        supported_language=language.strip()
                    )
                    supported_languages_objects.append(language_object)

                # Create or get full audio languages
                full_audio_languages = self.parse_list(row["Full audio languages"])
                full_audio_languages_objects = []
                for language in full_audio_languages:
                    language_object, _ = FullAudioLanguage.objects.get_or_create(
                        full_audio_language=language.strip()
                    )
                    full_audio_languages_objects.append(language_object)

                # Create or get developers
                developers = self.parse_list(row["Developers"])
                developer_objects = []
                for developer in developers:
                    developer_object, _ = Developer.objects.get_or_create(
                        developer=developer.strip()
                    )
                    developer_objects.append(developer_object)

                # Create or get publishers
                publishers = self.parse_list(row["Publishers"])
                publisher_objects = []
                for publisher in publishers:
                    publisher_object, _ = Publisher.objects.get_or_create(
                        publisher=publisher.strip()
                    )
                    publisher_objects.append(publisher_object)

                # Create or get categories
                categories = self.parse_list(row["Categories"])
                category_objects = []
                for category in categories:
                    category_object, _ = Category.objects.get_or_create(
                        category=category.strip()
                    )
                    category_objects.append(category_object)

                # Create or get genres
                genres = self.parse_list(row["Genres"])
                genre_objects = []
                for genre in genres:
                    genre_object, _ = Genre.objects.get_or_create(genre=genre.strip())
                    genre_objects.append(genre_object)

                # Create or get tags
                tags = self.parse_list(row["Tags"])
                tag_objects = []
                for tag in tags:
                    tag_object, _ = Tag.objects.get_or_create(tag=tag.strip())
                    tag_objects.append(tag_object)

                # Create the game
                game = Game.objects.create(
                    name=row["Name"],
                    release_date=self.clean_date(row["Release date"]),
                    estimated_owners=self.extract_estimated_owners(
                        row["Estimated owners"]
                    ),
                    peak_concurrent_users=row["Peak CCU"],
                    required_age=row["Required age"],
                    price=row["Price"],
                    dlc_count=row["DLC count"],
                    about_the_game=row["About the game"],
                    header_image=row["Header image"],
                    website=row["Website"],
                    support_url=row["Support url"],
                    support_email=row["Support email"],
                    windows=self.parse_boolean(row["Windows"]),
                    mac=self.parse_boolean(row["Mac"]),
                    linux=self.parse_boolean(row["Linux"]),
                    metacritic_score=row["Metacritic score"],
                    metacritic_url=row["Metacritic url"],
                    positive_ratings=row["Positive"],
                    negative_ratings=row["Negative"],
                    achievements=row["Achievements"],
                    average_playtime=row["Average playtime forever"],
                    median_playtime=row["Median playtime forever"],
                )

                # Add many-to-many relationships
                game.supported_languages.set(supported_languages_objects)
                game.full_audio_languages.set(full_audio_languages_objects)
                game.developers.set(developer_objects)
                game.publishers.set(publisher_objects)
                game.categories.set(category_objects)
                game.genres.set(genre_objects)
                game.tags.set(tag_objects)

                self.stdout.write(f"Imported {game.name}")
