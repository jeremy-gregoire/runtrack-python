def enlever_doublons(la_liste: list) -> list:
  """
  Enlève les doublons dans une liste de nombre.

  #### Parameters
   - la_liste : list > La liste dont il faut retirer les doublons.
  
  #### Returns
  list > La liste nettoyé.
  """
  registre = []

  for nombre in la_liste:
    # Si le nombre est déjà enregistré
    if nombre in registre:
      continue
    
    # Si le nombre n'est pas déjà enregistré
    registre.append(nombre)
  
  # Retourne le registre
  return registre

# Ma liste de nombre
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Affiche la liste actuel
print("La liste actuel:", L)

# Enlève les doublons
L = enlever_doublons(L)

# Affiche la liste de nombre sans les doublons
print("La liste modifier:", L)