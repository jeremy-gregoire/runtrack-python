def positif_ou_negatif(nombre: float) -> None:
  """
  Affiche si le nombre est positif ou négatif.

  #### Parameters
   - nombre : float > Une expression numérique correspondant au nombre à tester.
  """
  if nombre == 0:
    return
  
  if nombre < 0:
    print("négatif")
    return
  
  print("positif")

# Les différents tests pour ce programme
positif_ou_negatif(14)
positif_ou_negatif(1.4)
positif_ou_negatif(-0.14)
positif_ou_negatif(-14)