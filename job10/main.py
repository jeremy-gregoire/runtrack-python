montant_initial_invest=25_000
taux_rend_annuel=1.1
gain_annuel=(montant_initial_invest*taux_rend_annuel)*12

print(gain_annuel)

montant_initial_invest+=5_000
taux_rend_annuel+=0.02
gain_annuel=(montant_initial_invest*taux_rend_annuel)*12

print(gain_annuel)

taux_rend_annuel-=0.1
gain_annuel=((montant_initial_invest*taux_rend_annuel)*12)*(1-0.1)

print(gain_annuel)

