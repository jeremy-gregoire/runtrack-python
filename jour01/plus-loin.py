# Demande une phrase à l'utilisateur
phrase = input("Votre phrase: ")

# Si dans ma phase je possède au moin un "e"
if "e" in phrase:
    # Crée une somme des lettres pour récupèrer combien de lettre "e" il y a dans la phrase
    somme_lettres = 0

    # Pour chaque lettre dans ma phrase
    for c in phrase:
        # Ajoute 1 à la somme si la lettre est un "e"
        if c == "e":
            somme_lettres += 1

    # Affiche la bonne orthographe de la phrase de retour en fonction du nombre de lettre "e"
    if somme_lettres > 1:
        print("Votre phrase comporte " + str(somme_lettres) + " lettres 'e' à l'intérieur !")
    else:
        print("Votre phrase comporte une lettre 'e' à l'intérieur !")
else:
    print("Votre phrase ne comporte pas de lettre 'e' à l'intérieur !")
