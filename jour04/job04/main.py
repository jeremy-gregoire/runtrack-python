def afficher_la_liste() -> None:
    # Création d'une liste de fruits initiale
    fruits = ["pomme", "cerise", "orange", "melon"]
    
    # Affichage de la liste de fruits initiale
    print("Ma liste de base:", fruits)

    # Insertion du mot "mangue" à l'indice 2 de la liste (avant l'élément "orange")
    fruits.insert(2, "mangue")
    
    # Affichage de la liste de fruits après l'ajout de "mangue"
    print("Ma liste après ajout:", fruits)

# Appel de la fonction afficher_la_liste
afficher_la_liste()
