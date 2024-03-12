from django.shortcuts import get_object_or_404, redirect, render
from stockapp.models import Categorie, Produit, Stock
from django.contrib import messages



 # Affiche la page d'accueil.
def index(request):
    return render(request, 'stockapp/index.html')



 # Affiche la page liste_categorie
def list_categorie(request):
    categories = Categorie.objects.all()
    context={"categories":categories}

    return render(request, 'stockapp/list_categorie.html', context)

 # la page liste_categorie
def detail_categorie(request, id):
    categorie = Categorie.objects.get(id=id)
    context={'categorie': categorie}

    return render(request, 'stockapp/detail_categorie.html', context)



# la page ajouter_categorie
def ajouter_categorie(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        image = request.FILES.get("image")
        designation = request.POST.get("designation")
        description = request.POST.get("description")

        # Traiter les données (validation, création, )
         # Créer une instance du modèle
        new_categorie = Categorie.objects.create(
         image=image, 
         designation=designation,
         description=description
        )

                # Afficher des messages de succès ou d'erreur
        if new_categorie:
            # Enregistrer l'objet
            new_categorie.save()
            messages.success(request, "Enregistrement réussi")
            return redirect('list_categorie')
        else:
            messages.error(request, "Enregistrement échoué")

    # Afficher le formulaire
    form = Categorie()
    return render(request, "stockapp/ajouter_categorie.html", {"form": form})

# fonction modifier categorie
def modifier_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == "POST":
        # Récupérer les données du formulaire de modification
        image = request.FILES.get("image")
        designation = request.POST.get("designation")
        description = request.POST.get("description")

        # Mettre à jour les données de la catégorie
        categorie.image = image
        categorie.designation = designation
        categorie.description = description
        categorie.save()

        messages.success(request, "Catégorie modifiée avec succès.")
        return redirect('list_categorie')  # Redirige vers la liste des catégories

    return render(request, 'stockapp/modifier_categorie.html', {'categorie': categorie})

# fonction supprimer categorie
def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == "POST":
        categorie.delete()
        messages.success(request, "Catégorie supprimée avec succès.")
        return redirect('list_categorie')  # Redirige vers la liste des catégories
    return render(request, 'stockapp/supprimer_categorie.html', {'categorie': categorie})




 # Afficher la page liste_produit   
def list_produit(request):
    produits = Produit.objects.all()

    return render(request, 'stockapp/list_produit.html', context={"produits": produits})


#la page detail_produit
def detail_produit(request, pk):
    prod = Produit.objects.get(id=pk)
    context={'produit': prod}

    return render(request, 'stockapp/detail_produit.html', context)


#fonction ajouter produit
def ajouter_produit(request):
  
  if request.method == 'POST':
    # Récupération des données du formulaire
    reference = request.POST.get('reference')
    designation = request.POST.get('designation')
    categorie_id = request.POST.get('categorie')
    description = request.POST.get('description')
    prix_achat = request.POST.get('prix_achat')
    prix_vente = request.POST.get('prix_vente')
    stock_min = request.POST.get('stock_min')
    stock_max = request.POST.get('stock_max')
    image = request.FILES.get('image')

    # Traitement des données
    try:
      categorie = Categorie.objects.get(pk=categorie_id)
    except Categorie.DoesNotExist:
      messages.error(request, "Catégorie inexistante")
      return redirect('ajouter_produit')

    # Création du produit
    produit = Produit.objects.create(
      reference=reference,
      designation=designation,
      categorie=categorie,
      description=description,
      prix_achat=prix_achat,
      prix_vente=prix_vente,
      stock_min=stock_min,
      stock_max=stock_max,
      image=image,
    )

    # Enregistrement du produit
    if produit:
      messages.success(request, "Produit ajouté avec succès")
      return redirect('list_produit')
    else:
      messages.error(request, "Echec de l'ajout du produit")

  # Récupération des catégories
  categories = Categorie.objects.all()

  # Contexte de la page
  context = {'categories': categories}

  # Affichage du formulaire
  return render(request, 'stockapp/ajouter_produit.html', context)



# afficher les 10 derniers mouvements
def mouvement_stock(request):
    mouvements = Stock.objects.all().order_by('-date')[:10]
    context = {'mouvements': mouvements}

    return render(request, 'stockapp/mouvement_stock.html', context)



# fonction supprimer produit
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == "POST":
        produit.delete()
        messages.success(request, "Catégorie supprimée avec succès.")
        return redirect('list_produit')  # Redirige vers la liste des produits
    return render(request, 'stockapp/supprimer_produit.html', {'produit': produit})




def ajouter_stock(request):
   
  if request.method == 'POST':
    # Récupération des données du formulaire
    produit_id = request.POST.get('produit')
    quantite = request.POST.get('quantite')
    type_mouvement = request.POST.get('type_mouvement')
    
    # Traitement des données
    try:
      produit = Produit.objects.get(pk=produit_id)
    except Produit.DoesNotExist:
      messages.error(request, "Produit inexistant")
      return redirect('ajouter_stock')

    # Création du stock
    stock = Stock.objects.create(
      produit=produit,
      quantite=quantite,
      type_mouvement=type_mouvement,
    )

    # Enregistrement du stock
    if stock:
      messages.success(request, "Stock ajouté avec succès")
      return redirect('mouvement_stock')
    else:
      messages.error(request, "Echec de l'ajout du stock")

  # Récupération des produits
  produits= Produit.objects.all()

  # Contexte de la page
  context = {'produits': produits}

  # Affichage du formulaire
  return render(request, 'stockapp/ajouter_stock.html', context)

   
