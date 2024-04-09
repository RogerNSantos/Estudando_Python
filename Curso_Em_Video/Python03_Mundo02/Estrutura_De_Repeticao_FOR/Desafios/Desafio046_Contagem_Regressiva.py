""" Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artiofícios,
 indo de 10 ATÉ 0, com uma pausa de 1 SEFUNDO entre eles.
  """
from time import sleep
print('<-<- CONTAGEM REGRESSIVA ->->')
for cont in range(10, 0, -1): # -1 no lugar do 0 para contagem ir ate 0
    print(cont)
    sleep(1)
print('BUM! BUM! POW!')
