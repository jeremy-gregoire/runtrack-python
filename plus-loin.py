phrase = input("Votre phrase: ")

if "e" in phrase:
    compte_lettre = 0

    for c in phrase:
        if c == "e":
            compte_lettre += 1

    if compte_lettre > 1:
        print(
            "Votre phrase comporte "
            + str(compte_lettre)
            + " lettres 'e' à l'intérieur !"
        )
    else:
        print("Votre phrase comporte une lettre 'e' à l'intérieur !")
else:
    print("Votre phrase ne comporte pas de lettre 'e' à l'intérieur !")
