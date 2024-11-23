from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from api.models import Game

class Command(BaseCommand):
    help = 'Import games from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('game_csv', type=str, help='Path to the game CSV file')

    def handle(self, *args, **options):
        game_csv = options['game_csv']
        
        with open(game_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    try:
                        release_date = datetime.strptime(row['Release date'], '%b %d, %Y').strftime('%Y-%m-%d')
                    except ValueError:
                        release_date = datetime.strptime(row['Release date'], '%b %Y').strftime('%Y-%m-1')
                    
                    windows = row['Windows'].lower() == 'true'
                    mac = row['Mac'].lower() == 'true'
                    linux = row['Linux'].lower() == 'true'
                    
                    Game.objects.create(
                        name=row['Name'],
                        release_date=release_date,
                        estimated_owners=row['Estimated owners'],
                        peak_ccu=row['Peak CCU'],
                        required_age=row['Required age'],
                        price=float(row['Price']) if row['Price'] else 0.0,
                        dlc_count=row['DLC count'],
                        about_the_game=row['About the game'],
                        supported_languages=row['Supported languages'],
                        full_audio_languages=row['Full audio languages'],
                        reviews=row['Reviews'],
                        header_image=row['Header image'],
                        website=row['Website'],
                        support_url=row['Support url'],
                        support_email=row['Support email'],
                        windows=windows,
                        mac=mac,
                        linux=linux,
                        metacritic_score=row['Metacritic score'] or None,
                        metacritic_url=row['Metacritic url'],
                        user_score=row['User score'] or None,
                        positive=row['Positive'] or None,
                        negative=row['Negative'] or None,
                        achievements=row['Achievements'] or None,
                        recommendations=row['Recommendations'] or None,
                        notes=row['Notes'],
                        average_playtime_forever=row['Average playtime forever'] or None,
                        average_playtime_two_weeks=row['Average playtime two weeks'] or None,
                        median_playtime_forever=row['Median playtime forever'] or None,
                        median_playtime_two_weeks=row['Median playtime two weeks'] or None,
                        developers=row['Developers'],
                        publishers=row['Publishers'],
                        categories=row['Categories'],
                        genres=row['Genres'],
                        tags=row['Tags'],
                        screenshots=row['Screenshots'],
                        movies=row['Movies']
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error importing game {row["Name"]}: {str(e)}')
                    )
                    continue

            self.stdout.write(
                self.style.SUCCESS('Successfully imported games data')
            )