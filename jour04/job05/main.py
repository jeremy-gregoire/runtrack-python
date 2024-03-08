L = [ 14, 7, 41, 404, 48]

print("La liste actuel:", L)
print("Le 2eme élèment de la liste:", L[1])

def remplacer_avec_somme() -> None:
  somme = 0

  somme += L[2]
  somme += L[4]
  
  L[3] = somme

remplacer_avec_somme()
print("Liste après remplacement:", L)
print("La dernière valeur de la liste:", L[len(L) - 1])