def my_len(la_liste: list) -> int:
  """
  Récupère le nombre d'élèment dans ma liste.

  #### Parameters
   - la_liste : list > La liste pour récupère son nombre d'élèment.
  
  #### Returns
  int > Un entier correspondant au nombre d'élèment.
  """
  len = 0

  for _ in la_liste:
    len += 1
  
  return len

def trier_croissant(la_liste: list) -> None:
  """
  Trie une liste de nombre.

  #### Parameters
   - la_liste : list > La liste à trier.
  """
  # La taille de la liste
  list_len = my_len(la_liste)

  for _ in la_liste:
    i = 0
    for _ in la_liste:
      # Va pas plus si que le bout de la liste
      if i == list_len - 1:
        break

      # Intervertie les deux variables entre eux
      if la_liste[i + 1] < la_liste[i]:
        tmp = la_liste[i]
        la_liste[i] = la_liste[i + 1]
        la_liste[i + 1] = tmp
    
      i += 1

# Ma liste de nombre
L = [ 145, 321, 102, 6, 3, 75, 45, 91]

# Affiche la liste de nombre actuel
print("La liste actuel:", L)

# Fais le triage de la liste de nombre
trier_croissant(L)

# Affiche la liste de nombre après triage
print("La liste trier par ordre croissant:", L)