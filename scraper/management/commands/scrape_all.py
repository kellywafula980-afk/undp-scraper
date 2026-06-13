from django.core.management.base import BaseCommand
from django.core.management import call_command
from datetime import datetime

class Command(BaseCommand):
    help = 'Run all scrapers'
    
    def handle(self, *args, **options):
        start = datetime.now()
        self.stdout.write(f'Starting all scrapers at {start}')
        
        # Run scrapers
        call_command('scrape_sports')
        call_command('scrape_scholarships')
        
        end = datetime.now()
        self.stdout.write(self.style.SUCCESS(f'All scrapers completed in {(end-start).seconds} seconds'))
