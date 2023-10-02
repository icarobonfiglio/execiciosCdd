hora=24
horai=int(input("Hora de inicio da partida: "))
horaf=int(input("Hora de termino da partida: "))
if horaf<horai:
  duracao_jogo = (hora - horai) + horaf
  print(duracao_jogo)

else:
  duracao_jogo = horaf - horai
  print(duracao_jogo)