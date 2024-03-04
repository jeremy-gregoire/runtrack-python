montant_initial_investissement = float(input("Entrez le montant initial de l'investissement: "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel (en poucentage): "))

# Affiche le gain annuel en fonction du taux de rendement dans le terminal
gain_annuel = (montant_initial_investissement * 12) * (1 - (taux_rendement_annuel / 100))
print(" > Gain annuel (première étape): " + str(gain_annuel))

# Augmentation du capital de l'investisseur de 5 000 €
montant_initial_investissement += 5_000

# Augmentation du taux de rendement à 2%
taux_rendement_annuel += 0.02

# Calcule à nouveau le nouveau gain de l'investisseur
gain_annuel = (montant_initial_investissement * 12) * (1 - (taux_rendement_annuel / 100))

# Affiche le résultat dans le terminal
print(" > Gain annuel (deuxième étape): " + str(gain_annuel))

# Retrait de 10% du montant total par l'investisseur
montant_initial_investissement *= (1 - 0.1)

# Diminution du taux de rendement de 1% suite à ce retrait
taux_rendement_annuel -= 0.01

# Calcule du montant final de l'investissement
gain_annuel = (montant_initial_investissement * 12) * (1 - (taux_rendement_annuel / 100))

# Affiche le nouveau gain
print(" > Gain annuel (étape finale): " + str(gain_annuel))


