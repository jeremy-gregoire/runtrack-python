def remplacer_avec_somme() -> None:
  # Initialise une variable somme à 0
  somme = 0

  # Ajoute les éléments aux indices 2 et 4 de la liste L à la variable somme
  somme += L[2]
  somme += L[4]

  # Remplace l'élément à l'indice 3 de la liste L par la valeur de la variable somme
  L[3] = somme

# Initialisation de la liste L avec des valeurs
L = [14, 7, 41, 404, 48]

# Affichage de la liste initiale et du 2e élément de la liste
print("La liste actuelle:", L)
print("Le 2e élément de la liste:", L[1])

# Appel de la fonction remplacer_avec_somme
remplacer_avec_somme()

# Affichage de la liste après remplacement et de la dernière valeur de la liste
print("Liste après remplacement:", L)
print("La dernière valeur de la liste:", L[len(L) - 1])
