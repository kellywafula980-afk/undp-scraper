from django.db import models
from django.utils import timezone

class ScrapedItem(models.Model):
    CATEGORY_CHOICES = [
        ('scholarship', 'Scholarship'),
        ('sports', 'Sports'),
        ('news', 'News'),
        ('internship', 'Internship'),
        ('un_agency', 'UN Agency'),
    ]
    
    SOURCE_CHOICES = [
        ('undp_news', 'UNDP News'),
        ('mastercard_scholarship', 'Mastercard Scholarship'),
        ('espn_football', 'ESPN Football'),
        ('bbc_cricket', 'BBC Cricket'),
        ('unicef_careers', 'UNICEF Careers'),
    ]
    
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    url = models.URLField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    published_date = models.DateTimeField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    match_result = models.CharField(max_length=100, blank=True)
    score = models.CharField(max_length=50, blank=True)
    deadline = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=200, blank=True)
    eligibility = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    times_viewed = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-scraped_at']
    
    def __str__(self):
        return self.title[:100]

class ScrapingLog(models.Model):
    source = models.CharField(max_length=100)
    items_found = models.IntegerField(default=0)
    items_new = models.IntegerField(default=0)
    items_updated = models.IntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    success = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.source} - {self.started_at}"
