# La classe produit pour créer des produits
class Produit:
  def __init__(self,nom,prix_unitaire,quantite_en_stock) -> None:
    self.nom=nom
    self.prix_unitaire=prix_unitaire
    self.quantite_en_stock=quantite_en_stock
  
  def afficher(self) -> None:
    print("Nom du produit: "+self.nom+"\nPrix unitaire: "+str(self.prix_unitaire)+"\nQuantité en stock: "+str(self.quantite_en_stock))

# Le produit à afficher
mon_produit=Produit("Cassoulet", 2_000_000.45, 2_000)

# Affiche les informations du produits par défaut
mon_produit.afficher()

# Applique l'inflation au produit
print("===================== INFLATION =====================")
mon_produit.prix_unitaire*=1.1

# Affiche les informations du produits avec les modifications de l'inflation
mon_produit.afficher()