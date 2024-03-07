def calcule(num1: float, operator: str, num2: float) -> float:
  """
  Calcule le résultat d'une opération de deux nombres.

  #### Parameters
   - num1 : float > Une expression numérique correspondant au premier nombre de l'opération.
   - operator : str > L'opérateur de l'opération (addition, soustraction, multiplication, division et le reste de la division).
   - num2 : float > Une expression numérique correspondant au deuxième nombre de l'opération.
  
  #### Returns

  Le résultat de l'opération en fonction de l'opérateur.
  """

  match operator:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      return num1 / num2
    case "%":
      return num1 % num2
    case _:
      return None

# Les différents tests pour ce programme
print(calcule(4, "+", 8))
print(calcule(4, "-", 8))
print(calcule(4, "*", 8))
print(calcule(4, "/", 8))
print(calcule(4, "%", 8))