def quelle_developpeur_es_tu(langage: str) -> None:
  """
  Affiche l'état du développeur en fonction du langage de programmation.
  
  #### Parameters
   - langage: string > Le nom du langage de programmation
  """

  match langage:
    case "javascript":
      print("tu es un développeur web")
      return
    case "python":
      print("tu es un dévelopeur IA")
      return
    case "java":
      print("tu es un dévelopeur logiciel")
      return
    case "reactjs":
      print("tu es un dévelopeur mobile")
      return
    case _:
      print("un jour, je serai le meilleur développeur...")
      return

# Les différents tests pour ce programme
quelle_developpeur_es_tu("test")
quelle_developpeur_es_tu("javascript")
quelle_developpeur_es_tu("python")
quelle_developpeur_es_tu("java")
quelle_developpeur_es_tu("reactjs")