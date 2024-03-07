def moyenne(note1: float, note2: float, note3: float) -> float:
  """
  Retourne le calcule de moyenne de trois notes.

  #### Parameters
   - note1 : float > Une expression numérique correspondant la note n°1.
   - note2 : float > Une expression numérique correspondant la note n°2.
   - note3 : float > Une expression numérique correspondant la note n°3.
  
  #### Returns

  La moyenne de ces trois notes.
  """
  return (note1 + note2 + note3) / 3

# Demande à l'utilisateur d'entre trois notes.
note1 = float(input("Entrez la note n°1: "))
note2 = float(input("Entrez la note n°2: "))
note3 = float(input("Entrez la note n°3: "))

# Calcule la moyenne de ces trois notes
moyenne_etudiant = moyenne(note1, note2, note3)

# Indique si c'est l'état de l'étudiant en fonction de sa moyenne
if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
  print("Très bon élève")
elif moyenne_etudiant >= 11 and moyenne_etudiant < 14:
  print("Bon élève")
elif moyenne_etudiant >= 8 and moyenne_etudiant < 10:
  print("Élève moyen")
else:
  print("Élève devant faire des efforts")