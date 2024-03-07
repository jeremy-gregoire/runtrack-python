def inverser_une_chaine(chaine: str) -> str:
  """
  Retourne une version inversé d'une chaine de caractère.

  #### Parameters
   - chaine : string > La chaine de caractère qui va servir à retourner sa version inversé.
  
  #### Returns

  La version inversé de la chaine de caractère passer en paramètre.
  """
  return chaine[::-1]

# Affiche la chaine inverser de "nikana"
print(inverser_une_chaine("nikana"))