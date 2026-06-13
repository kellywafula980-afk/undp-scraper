from django.shortcuts import render
from scraper.models import ScrapedItem
from django.db.models import Q

def index(request):
    query = request.GET.get('q', '')
    
    items = ScrapedItem.objects.filter(is_active=True)
    
    # Exclude messy sports data
    items = items.exclude(
        Q(title__icontains='Postponed') |
        Q(title__icontains='ABB') |
        Q(title__icontains='LIVE') |
        Q(title__icontains='vs v')
    )
    
    if query:
        items = items.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    categories = {
        'sports': items.filter(category='sports')[:10],
        'scholarship': items.filter(category='scholarship')[:10],
        'internship': items.filter(category='internship')[:10],
        'news': items.filter(category='news')[:5],
    }
    
    recent_updates = items.order_by('-scraped_at')[:20]
    
    context = {
        'categories': categories,
        'recent_updates': recent_updates,
        'search_query': query,
        'total_count': items.count(),
    }
    
    return render(request, 'web/index.html', context)
