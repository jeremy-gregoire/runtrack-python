limite = 100

# Pour chaque nombre de 1 jusqu'à 100
for i in range(1, limite + 1):
  # Si i est un multiple de 3
  if i % 3 == 0:
    print(str(i) + " : Fizz")
    continue
  
  # Sinon, si i est un multiple de 5
  if i % 5 == 0:
    print(str(i) + " : Buzz")
  
  # Sinon, i est n'y un multiple de 3 et de 5
  print(str(i) + " : FizzBuzz")