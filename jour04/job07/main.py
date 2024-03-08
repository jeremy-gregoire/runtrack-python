# Initialisation d'une liste L de nombres
L = [8, 24, 48, 2, 16]

# Initialisation d'une variable pour compter le nombre de multiples de 3
nb_multiples = 0

# Affichage de la liste initiale
print("La liste actuelle:", L)

# Parcours de la liste pour compter les multiples de 3
for nombre in L:
  if nombre % 3 == 0:
    nb_multiples += 1

# Affichage du nombre de multiples de 3
print("Il y a", nb_multiples, "multiples" if nb_multiples > 1 else "multiple", "de 3")
