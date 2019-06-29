from django.contrib import admin
from django.urls import path, include
import page.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('tutorboard/', include('tutorboard.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
