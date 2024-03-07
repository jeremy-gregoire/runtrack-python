# Demande à l'utilisateur d'entrer le côté adjacent
adjacent = float(input("Côté adjacent: "))

# Demande à l'utilisateur d'entrer le côté opposé
oppose = float(input("Côté opposé: "))

# Demande à l'utilisateur d'entrer l'hypoténuse
hypotenuse = float(input("Côté hypoténuse: "))

# Détermine s'il est possible de construire un triangle avec ces longueurs
if adjacent <= 0 and oppose <= 0 and hypotenuse <= 0:
  print("Il est impossible de construire un triangle avec ces longueurs !")
  exit()

# Une variable permettant de tester si le triangle est isocèle ou non
isocele = adjacent == oppose or oppose == hypotenuse or hypotenuse == adjacent

# Un variable permettant de tester si le triangle est rectangle ou non
rectangle = adjacent**2 + oppose**2 == hypotenuse**2 or oppose**2 + hypotenuse**2 == adjacent**2 or hypotenuse**2 + adjacent**2 == oppose**2

# Détermine si le triangle est un triangle équilatéral
if adjacent == oppose == hypotenuse:
  print("Ce triangle est un triangle équilatéral !")

# Détermine si le triangle est un triangle rectangle isocèle
elif isocele and rectangle:
  print("Ce triangle est un triangle rectange isocèle !")

else:
  # Détermine si le triangle est un triangle isocèle
  if isocele:
    print("Ce triangle est un triangle isocèle !")

  # Détermine si le triangle est un triangle rectangle
  elif rectangle:
    print("Ce triangle est un triangle rectange !")

  # Détermine si le triangle est un triangle quelconque
  else:
    print("Ce triangle est un triangle quelconque !")
