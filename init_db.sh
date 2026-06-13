#!/bin/bash
# This script creates the database and runs migrations

python manage.py makemigrations scraper
python manage.py migrate

# Check if database is empty (no sports items)
if [ $(python manage.py shell -c "from scraper.models import ScrapedItem; print(ScrapedItem.objects.filter(category='sports').count())") -eq 0 ]; then
    echo "Database empty, running scrapers..."
    python manage.py scrape_sports
    python manage.py scrape_scholarships
fi
