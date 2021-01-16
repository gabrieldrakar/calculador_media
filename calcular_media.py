def entrada_de_notas():
  nota1 = float(input('primeira nota '))
  nota2 = float(input('segunda nota '))
  return calcular_media(nota1,nota2)

def calcular_media(nota1,nota2):
  media = (nota1 + nota2) / 2
  print(media)
  return media

def calcular_aprovacao(media):
  if(media >= 6):
    print('aprovado')
  else:
    print('reprovado')

minha_media=media()
calcular_aprovacao(minha_media)