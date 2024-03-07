limite = 100
exclus = [ 26, 37, 88 ]

# Affiche les nombres de 0 à 100 y compris mais le 26, 37 et 88 sont pas affiché
for i in range(limite + 1):
  if i in exclus:
    continue
  
  print(i)