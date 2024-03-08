def est_paire(nombre: float) -> bool:
  """
  Vérifie si un nombre est pair.

  #### Parameters:
   - nombre : float > Le nombre à vérifier.

  #### Returns:
  bool > True si le nombre est pair, False sinon.
  """
  return nombre % 2 == 0

# Ma liste de nombre
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# La somme des nombres pairs
somme = 0

# Affichage de la liste initiale
print("La liste actuelle:", L)

# Pour chaque nombre dans ma liste de nombre
for nombre in L:
  # Si le nombre est paire
  if not est_paire(nombre):
    continue

  # Ajout du nombre pair à la somme
  somme += nombre

# Affiche de la somme des nombres pairs
print("La somme des nombres pairs:", somme)
