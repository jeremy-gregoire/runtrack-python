# Création d'une liste L contenant les entiers de 1 à 5 à l'aide d'une compréhension de liste
L = [i for i in range(1, 6)]

# Affichage de la liste initiale
print("La liste actuelle:", L)

# Échange du premier et du dernier élément de la liste en utilisant une variable temporaire
tmp = L[0]
L[0] = L[len(L) - 1]
L[len(L) - 1] = tmp

# Affichage de la liste après les changements
print("La liste avec les changements:", L)
