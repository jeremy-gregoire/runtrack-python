def afficher_la_liste() -> None:
  fruits = [ "pomme", "cerise", "orange", "melon" ]
  print("Ma liste de base:", fruits)

  fruits.insert(2, "mangue")
  print("Ma liste après ajout:", fruits)

afficher_la_liste()