maca=1.30
compra=int(input("Digite o numero de maçãs que você deseja: "))
if compra>=12:
  maca=maca-0.30
  total=maca*compra
  print(f"Total a ser pago é de R$ {total}")
else:
  total=maca*compra
  print(f"Total a ser pago é de R$ {total}")