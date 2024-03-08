def taille(object: str | list) -> int:
  len: int = 0

  for _ in object:
    len += 1
  
  return len

def trier_croissant(list: list) -> None:
  list_len = taille(list)

  for _ in list:
    i = 0
    for _ in list:
      if i == list_len - 1:
        break

      if list[i + 1] < list[i]:
        tmp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = tmp
    
      i += 1

def arrondir(n):
  entier = int(n)
  decimal = n - entier

  if decimal >= 0.5:
    entier += 1
  
  return entier

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("La liste actuel:", L)

i = 0
for nombre in L:
  L[i] = arrondir(nombre)
  i += 1

print("La liste arrondie:", L)

trier_croissant(L)
print("La liste arrondie et dans l'ordre croissant:", L)