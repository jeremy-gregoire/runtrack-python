def est_paire(nombre: float) -> bool:
  return nombre % 2 == 0

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme = 0

print("La liste actuel:", L)

for nombre in L:
  if not est_paire(nombre):
    continue

  somme += nombre

print("La somme des nombres paire:", somme)