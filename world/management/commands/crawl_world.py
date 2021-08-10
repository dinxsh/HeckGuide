from django.core.management.base import BaseCommand
from world.importer import WorldImporter

from django.conf import settings


class Command(BaseCommand):
    help = 'Crawl through the world using selected token'

    def add_arguments(self, parser):
        parser.add_argument('token',  type=int)

    def handle(self, *args, **options):
        """
        Usage: python manage.py crawl_world token "2"
        """
        if options['token'] == 1:
            token = settings.HECKFIRE_API_TOKEN
            staytoken = settings.STAY_ALIVE_TOKEN
        elif options['token'] == 2:
            token = settings.TOKEN_128
            staytoken = settings.STAY_128
        importer = WorldImporter(token=token, staytoken=staytoken)
        importer.execute(lowerbound=1868, upperbound=6328)