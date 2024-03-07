# Demande à l'utilisateur combien de table de multiplication à afficher
n_table = int(input("Combien de table de multiplication voulez-vous affiché ? "))

# Nombre de multiplication pour chaque table
n_multiplication = int(input("Combien de multiplication voulez-vous pour chaque table ? "))

# Si l'utilisateur mets une valeur inférieur ou égale à 0 pour le nombre de table de multiplication
if n_table <= 0:
  n_table = 1

# Si l'utilisateur mets une valeur inférieur ou égale à 0 pour le nombre de multiplication par table
if n_multiplication <= 0:
  n_multiplication = 10

# Affiche la table de 1 jusqu'à N
for n in range(1, n_table + 1):
  print("\nTable de multiplication de " + str(n))

  # Affiche la multiplication de 1 à 10 de la table de multiplication n
  for i in range(1, n_multiplication + 1):
    print(str(n) + " x " + str(i) + " = " + str(n * i))