montant_initial_invest=float(input("Montant initial de l'investissement: "))
taux_rend_annuel=1+(float(input("Taux de rendement annuel: "))/100)
gain_annuel=(montant_initial_invest*taux_rend_annuel)*12

print(gain_annuel)

montant_initial_invest+=5_000
taux_rend_annuel+=0.02
gain_annuel=(montant_initial_invest*taux_rend_annuel)*12

print(gain_annuel)

taux_rend_annuel-=0.1
gain_annuel=((montant_initial_invest*taux_rend_annuel)*12)*(1-0.1)

print(gain_annuel)

