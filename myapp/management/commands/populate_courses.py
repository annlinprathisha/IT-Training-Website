
from django.core.management.base import BaseCommand
from myapp.views import save_courses

class Command(BaseCommand):
    help = 'Populates the database with courses'

    def handle(self, *args, **kwargs):
        save_courses()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with courses'))
