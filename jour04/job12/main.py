def my_len(list: list) -> int:
  len = 0
  for _ in list:
    len += 1
  return len

def trier_croissant(list: list) -> None:
  list_len = my_len(list)

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

L = [ 145, 321, 102, 6, 3, 75, 45, 91]
print("La liste actuel:", L)

trier_croissant(L)
print("La liste trier par ordre croissant:", L)