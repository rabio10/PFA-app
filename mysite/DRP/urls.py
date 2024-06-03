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
    path('create/', views.create_entrepot_central, name='create_entrepot_central'),
    #path('success/', TemplateView.as_view(template_name="success.html"), name='success'),  # Add a success page if needed

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)