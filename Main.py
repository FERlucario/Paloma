meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "algo raro o embarazoso",
            "SHEESH": "una respuesta a una broma",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
print("Saludos")
for i in range(5):
  word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
  if word in meme_dict.keys():
      print("Eso significa", meme_dict[word])
  else:
      print("Eso no está dentro del diccionario")
