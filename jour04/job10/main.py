# Ma liste de nombre
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

# Produit commence à 1 car s'il commencé par 0, le produit donnerai tous le temps 0
produit = 1

# Affiche la liste de nombre actuel
print("La liste actuel:", L)

# Pour chaque nombre dans ma liste de nombre
for nombre in L:
  # Fais le produit des nombres entre 25 et 90
  if nombre >= 25 and nombre <= 90:
    produit *= nombre

# Affiche la liste de nombre après le produit
print("Produit de toutes les valuers comprises entre 25 et 90:", produit)