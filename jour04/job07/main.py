L = [ 8, 24, 48, 2, 16 ]
nb_mutiples = 0

print("La liste actuel:", L)

for nombre in L:
  if nombre % 3 == 0:
    nb_mutiples += 1

print("Il y a", nb_mutiples, "multiples" if nb_mutiples > 1 else "multiple", "de 3")

