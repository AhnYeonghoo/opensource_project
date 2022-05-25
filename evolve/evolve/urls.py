
from django.contrib import admin
from django.urls import path, include
from search import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include("search.urls")),
    path('authenticated/', include("authenticated.urls")),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

