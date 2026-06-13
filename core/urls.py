from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    # Google verification route
    path('google56bce93523ece129.html', 
         TemplateView.as_view(template_name='google56bce93523ece129.html', 
         content_type='text/html')),
]

# Serve static files in production
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
