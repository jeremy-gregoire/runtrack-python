def afficher_la_liste() -> None:
  # Création d'une liste de fruits initiale
  fruits = ["pomme", "cerise", "orange"]
  
  # Affichage de la liste de fruits initiale
  print("Ma liste de base:", fruits)

  # Ajout du mot "Melon" à la fin de la liste
  fruits.append("Melon")
  
  # Affichage de la liste de fruits après l'ajout de "Melon"
  print("Ma liste après ajout:", fruits)

# Appel de la fonction afficher_la_liste
afficher_la_liste()