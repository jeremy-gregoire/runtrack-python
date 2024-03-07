""" PREMIER MÉTHODE POUR CETTE EXERCICE """
# Ma chaine de caractère pour former la pyramide
# chaine1 = "abcdefghijklmnopqrstuvwxyz" * 10

# Boucle jusqu'à la limite de la chaine de caractère
# for i in range(0, len(chaine1), 2):
#   print(chaine1[0:i-1])

""" DEUXIÈME MÉTHODE POUR CETTE EXERCICE """
# La chaine de caractère
chaine2 = "abcdefghijklmnopqrstuvwxyz"
# Nombre de ligne voulue
n_ligne = 32

# Pour chaque ligne
for i in range(0, n_ligne):
  # Crée une chaine de sortie
  sortie = ""

  # Nombre de caractère voulue après cette ligne
  n_caractere = i + 1

  # La vrai position des caractères
  idx = 0

  # Incrémental par défaut (pour récupérer un seul caractère en premier)
  incremental = 1

  # Pour chaque n caractère
  for j in range(0, n_caractere):
    # Réinitialise la vrai position s'il atteint la taille maximum de la chaine de caractère
    if idx >= len(chaine2):
      idx = 0

    # Passe à 2 de d'incrémental après la premier ligne
    if j > 0 and incremental != 2:
      incremental = 2

    # Crée la chaine de caractère de sortie en concatènant les caractères de la chaine de caractère de la vrai position à la vrai position plus l'incrémental
    sortie += chaine2[idx:idx+incremental]

    # Increment la vrai position
    idx += 1

  # Affiche la chaine de caractère de sortie
  print(sortie)

  # Incrémente le nombre de caractère voulue après cette ligne
  n_caractere += 1