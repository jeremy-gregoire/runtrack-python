# Une classe pour créer des produits
class Produit:
  def __init__(self, nom: str, prix_unitaire: float, quantite_en_stock: int) -> None:
    self.nom=nom
    self.prix_unitaire=prix_unitaire
    self.quantite_en_stock=quantite_en_stock
  
  def afficher(self) -> None:
    print("Nom du produit: " + self.nom+"\nPrix unitaire: " + str(self.prix_unitaire) + "\nQuantité en stock: " + str(self.quantite_en_stock))

print("==================== PRODUIT ACTUEL ====================")
# Crée et affiche un produit
mon_produit = Produit("Cassoulet", 5.45, 2_000)
mon_produit.afficher()

print("==================== AJOUT D'UN PRODUIT EN STOQUE ====================")
# Ajout d'un produit en stock et affiche le produit mis à jour
mon_produit.quantite_en_stock += 1
mon_produit.afficher()

print("==================== ACHETER LE PRODUIT ====================")
# Demande à l'utilisateur de saisir une quantité de produit qu'il souhaite acheter
quantite_achete_par_utilisateur = int(input("Combien voulez acheter ? "))

# Mets à jour les stocks du produit
mon_produit.quantite_en_stock -= quantite_achete_par_utilisateur
mon_produit.afficher()

# Affiche un bilan d'achat
print("==================== BILAN DE L'ACHAT ====================")
print("Quantité acheter: " + str(quantite_achete_par_utilisateur))
print("Prix unitaire du produit: " + str(mon_produit.prix_unitaire))
print("Prix total à payer: " + str(quantite_achete_par_utilisateur * mon_produit.prix_unitaire))

print("==================== LE PRIX DU PRODUIT AUGMENTE DE 10% ====================")
# Augmentation de 10% le prix du produit du à l'inflation
mon_produit.prix_unitaire *= 1.1
mon_produit.afficher()