import sys
from typing import NoReturn

from django.core.management.base import BaseCommand

from shinobi.parser.genre import AnimeGenreParser
from shinobi.utilities.session import session

from ...models.anime_genre import AnimeGenreModel


class Command(BaseCommand):
    help = "Django command that gets the Anime Genre Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "genre_id",
            type=int,
            help="The Genre ID number to get information for",
        )

    def handle(self, *args, **options) -> NoReturn:
        genre_id: int = options["genre_id"]
        res = self.client.get(f"https://myanimelist.net/anime/genre/{genre_id}")

        parser = AnimeGenreParser(res.text)
        data_dictionary = parser.build_dictionary()

        try:
            genre_instance = AnimeGenreModel.objects.get(mal_id=genre_id)
        except AnimeGenreModel.DoesNotExist:
            self.stdout.write(f"No GenreModel found for {self.style.ERROR(genre_id)}")
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(genre_instance, attr, value)

        genre_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(genre_id)}")
