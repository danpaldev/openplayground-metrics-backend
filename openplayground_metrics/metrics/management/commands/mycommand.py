from django.core.management.base import BaseCommand
from dotenv import load_dotenv
import os


class Command(BaseCommand):
    load_dotenv()

    def handle(self, *args, **kwargs):
        self.stdout.write(os.getenv('TEST'))
