L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
produit = 1

print("La liste actuel:", L)

for nombre in L:
  if nombre >= 25 and nombre <= 90:
    produit *= nombre

print("Produit de toutes les valuers comprises entre 25 et 90:", produit)