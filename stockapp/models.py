from django.db import models

# model catrgorie

class Categorie(models.Model):
      image = models.ImageField( upload_to="images", blank=True )
      designation = models.CharField(max_length=50)
      description = models.TextField(blank=True)

      def __str__(self):
            return self.designation


class Produit(models.Model):
      reference = models.IntegerField()
      designation = models.TextField(max_length=50)
      categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
      description = models.TextField(blank=True)
      prix_achat = models.FloatField(default=0.0)
      prix_vente = models.FloatField(default=0.0)
      stock_min = models.IntegerField()
      stock_max = models.IntegerField()
      image = models.ImageField( upload_to="images", blank=True )

      def __str__(self):
          return self.designation
      

class Stock(models.Model):
      produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
      quantite = models.IntegerField()
      date = models.DateTimeField(auto_now=True) 
      type_mouvement = models.CharField(max_length=50)  

      def __str__(self) :
            return self.type_mouvement
      

