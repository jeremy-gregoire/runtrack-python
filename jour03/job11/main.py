def time_to_text(minutes: int) -> None:
  """
  Affiche le temps en heure-minute dans la console (affichage sous la forme "X heures et Y minutes).

  #### Parameters
   - minutes : int > Une expression numérique correspondant au nombre de minutes à convertir.
  """
  # Calcule le nombre d'heures et de minutes
  heures = minutes // 60
  minute = int(((minutes / 60) - heures) * 60)

  # Génère le mot au pluriel des heures et minutes
  heures_str = "heures" if heures > 1 else "heure"
  minutes_str = "minutes" if minute > 1 else "minute"
  
  # Affiche sous le forme "X heure(s) et Y minute(s)"
  print(str(heures) + " " +  heures_str + " et " + str(minute)+ " " +  minutes_str)

# Les différents tests pour ce programme
time_to_text(360)
time_to_text(450)
time_to_text(60)
time_to_text(30)
time_to_text(750)
time_to_text(167)