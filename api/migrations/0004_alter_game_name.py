# Generated by Django 5.1.3 on 2024-12-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_game_about_the_game_alter_game_dlc_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
