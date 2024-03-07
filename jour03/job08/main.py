def affiche_aliment(type: str, saison: str) -> None:
  """
  Affiche les aliments en fonction de leur type et de la saison.

  #### Parameters
   - type : string > Le type de l'aliment (fruits ou légume)
   - saison : string > La saison de cette aliment (hiver ou été)
  """
  if type == "fruits":
    match saison:
      case "hiver":
        print("orange, mandarine et kiwi")
        return
      case "été":
        print("poire, fraise et cassis")
        return
      case _: # Si la saison n'existe pas
        print("La saison des fruits n'existe !")
        return
  
  elif type == "légume":
    match saison:
      case "hiver":
        print("carotte, topinambour et endive")
        return
      case "été":
        print("artichaut, aubergine et navet")
        return
      case _: # Si la saison n'existe pas
        print("La saison du légume n'existe !")
        return
  
  # Si le type n'existe pas
  else:
    print("Le type de fruit n'existe pas !")

# Les différents tests pour ce programme
affiche_aliment("fruits", "hiver")
affiche_aliment("légume", "hiver")
affiche_aliment("fruits", "été")
affiche_aliment("légume", "été")