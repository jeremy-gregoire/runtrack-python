def taille(objet: str | list) -> int:
  """
  Retourne la taille de l'objet.

  #### Parameters
   - object : str | list > L'objet qui peut être une chaine de caractère ou une liste.
  """
  len: int = 0

  for _ in objet:
    len += 1
  
  return len

def separer(chaine: str, separateur: str = " ") -> list:
  """
  Séparer chaque séquence de la chaine par rapport au séparateur.

  #### Parameters
   - chaine : str > La chaine de carctère à séparer.
   - separateur : str > Le séparateur dont la séparation sera enclencher.
  
  #### Returns
  list > La liste des séquences de la chaine.
  """
  mots = []
  mot = ""

  for c in chaine:
    # Ajoute un nouveau élément dans ma liste à chaque fois que le séparateur est rencontré
    if c == separateur:
      mots.append(mot)
      mot = ""
      continue
    
    # Ajoute les caractères qui ne sont pas des ponctuations
    if not c in [ ",", ".", "!", "?", "-" ]:
      mot += c
  
  # Retourne la liste de mot
  return mots

def joindre(la_liste: list, separateur: str = " ") -> str:
  """
  Join tous les éléments d'une liste pour obtenir une chaine de caractère.

  #### Parameters
   - mots : list > La liste dont on récupère les éléments.
   - separateur : str > Espacement entre chaque élément.
  
  #### Returns
  str : Une chaine de caractère avec les éléments.
  """
  chaine = ""
  taille_liste = taille(la_liste)s

  i = 0
  for mot in la_liste:
    if i == taille_liste - 1:
      chaine += mot
      break

    chaine += mot + separateur
    i += 1
  
  return chaine

def my_long_word(longueur: int, chaine: str) -> None:
  # Récupère une liste de mot
  mots = separer(chaine)

  # Une liste de correspondance
  corresp = []
s
  for mot in mots:
    # Si le mot se trouve déjà dans les correspondances
    if mot in corresp:
      continue
    
    # La taille de chaque mot
    len_mot = taille(mot)

    # Ajoute les mots ayant taille de longueur définie
    if len_mot >= longueur:
      corresp.append(mot)
  
  # Retourne la jointure de cette correspondance
  return joindre(corresp)

long_mot = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

# Affiche les mots long dans une chaine de caractère
print(long_mot)