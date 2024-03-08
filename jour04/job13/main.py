def enlever_doublons(list: list) -> list:
  registre = []

  for nombre in list:
    if nombre in registre:
      continue
    
    registre.append(nombre)
  
  return registre

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("La liste actuel:", L)

L = enlever_doublons(L)
print("La liste modifier:", L)