from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.DRP_app, name='DRP'),
    path('generale/', views.generale, name='generale'),
    path('prevision/', views.prevision, name='prevision'),
    path('historique/', views.historique, name='historique'),
    path('planification/', views.planification, name='planification'),
    path('parametre/', views.parametre, name='parametre'),
    path('prevision_total_json/', views.prevision_total_json, name='prevision_total_json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)