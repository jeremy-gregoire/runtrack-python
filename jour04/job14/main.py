def taille(object: str | list) -> int:
  len: int = 0

  for _ in object:
    len += 1
  
  return len

def separer(chaine: str, separateur: str = " ") -> list:
  mots = []
  mot = ""

  for c in chaine:
    if c == separateur:
      mots.append(mot)
      mot = ""
      continue
    
    if not c in [ ",", ".", "!", "?", "-" ]:
      mot += c
  
  return mots

def joindre(mots: list, separateur: str = " ") -> str:
  chaine = ""
  taille_liste = taille(mots)

  i = 0
  for mot in mots:
    if i == taille_liste - 1:
      chaine += mot
      break

    chaine += mot + separateur
    i += 1
  
  return chaine

def my_long_word(longueur: int, chaine: str) -> None:
  mots = separer(chaine)
  corresp = []

  for mot in mots:
    if mot in corresp:
      continue
    
    len_mot = taille(mot)

    if len_mot >= longueur:
      corresp.append(mot)
  
  return joindre(corresp)

long_mot = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(long_mot)