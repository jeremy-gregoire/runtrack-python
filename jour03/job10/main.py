def determine_nombre_impaire_ou_paire(nombre: int) -> None:
  """
  Détermine si un nombre est impaire ou pair et l'affiche dans la console.

  #### Parameters
   - nombre: int > Une expression numérique correspondant au nombre à tester.
  """

  # Les nombres ne doivent pas être négatif
  if nombre < 0:
    print("Le nombre doit être un entier positif !")
    return
  
  # Test le nombre s'il est paire ou non
  if nombre % 2 == 0:
    print("Le nombre est paire")
  else:
    print("Le nombre est impaire")

# Les différents tests pour ce programme
determine_nombre_impaire_ou_paire(4)
determine_nombre_impaire_ou_paire(7)
determine_nombre_impaire_ou_paire(0)
determine_nombre_impaire_ou_paire(-4)