from django.contrib import admin
from stockapp.models import Categorie, Produit, Stock 

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Stock)
