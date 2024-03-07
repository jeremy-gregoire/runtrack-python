def obtenir_nbs_premier(min: int, max: int) -> list:
  """
  Récupère une liste de nombre premier.

  #### Parameters

  - min : int > Intervale minimum de récupération des nombres premier.
  - max : int > Intervale maximum de récupération des nombres premier.
  
  #### Returns
  
  Une liste de nombre premier d'intervale mininum et maximum.
  """

  # Crée une liste vide de nombre premier
  nbs_premier = []
  
  # Pourquoi nombre de minimum jusqu'au maximum
  for i in range(min, max + 1):
    # Chaque nombre i crée un nombre de diviseurs initialisé à 0
    nb_diviseurs = 0

    # Pourquoi nombre de minimum jusqu'au maximum
    for n in range(min, max + 1):
      # Passe la boucle si le reste de la division de i et n est différent de 0 
      if i % n != 0:
        continue

      # Ajoute un diviseur si le reste de la division de i et n est égale à 0
      nb_diviseurs += 1
    
    # On ajoute i, si celui-ci à exactement 2 diviseurs
    if nb_diviseurs == 2:
      nbs_premier.append(i)
  
  # Retourne la liste
  return nbs_premier

# Nombre d'occurence pour les nombres premier
n_max = 100

# Une liste de nombre premier de 1 à n_max
nbs_premier = obtenir_nbs_premier(1, n_max)

# Affiche tous les nombres premier de ma liste
for nb_premier in nbs_premier:
  print(nb_premier)