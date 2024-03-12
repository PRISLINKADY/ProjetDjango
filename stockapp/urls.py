from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_categorie/', views.list_categorie, name='list_categorie'),
    path('detail_categorie/<int:id>/', views.detail_categorie, name='detail_categorie'),
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('modifier-categorie/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer_categorie/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('list_produit/', views.list_produit, name='list_produit'),
    path('detail_produit/<int:pk>/', views.detail_produit, name='detail_produit'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),  
     path('supprimer_produit/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('mouvement_stock/', views.mouvement_stock, name='mouvement_stock'),
    path('ajouter_stock/', views.ajouter_stock, name='ajouter_stock'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
