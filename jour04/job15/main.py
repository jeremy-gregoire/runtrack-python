def taille(object: str | list) -> int:
  """
  Retourne la taille de l'objet.

  #### Parameters
   - object : str | list > L'objet qui peut être une chaine de caractère ou une liste.
  """
  len: int = 0

  for _ in object:
    len += 1
  
  return len

def trier_croissant(list: list) -> None:
  """
  Trie une liste de nombre.

  #### Parameters
   - la_liste : list > La liste à trier.
  """
  list_len = taille(list)

  for _ in list:
    i = 0
    for _ in list:
      if i == list_len - 1:
        break

      if list[i + 1] < list[i]:
        tmp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = tmp
    
      i += 1

def arrondir(n: float) -> int:
  """
  Arrondie un nombre avec une décimale.

  #### Parameters
   - n : float > Un nombre floatant à arrondir.
  
  #### Returns
  int : Le nombre arrondie.
  """
  entier = int(n)
  decimal = n - entier

  if decimal >= 0.5:
    entier += 1
  
  return entier

# Ma liste de nombre
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Affiche la liste de nombre actuel
print("La liste actuel:", L)

# Arrondie chaque nombre de ma liste
i = 0
for nombre in L:
  L[i] = arrondir(nombre)
  i += 1

# Affiche la liste avec les nombres arrondient
print("La liste arrondie:", L)

# Trie la liste de nombre arrondie
trier_croissant(L)

# Affiche la liste de nombre arrondie et trier
print("La liste arrondie et dans l'ordre croissant:", L)