"""num = [2, 5, 7, 9]
num[2] = 1
num.append(10)   #Adicionando números
num.sort()   #Colocando em ordem crescente
num.insert(1, 9)   #Inserindo
if 10 in num:
    num.remove(10)
else:
    print(' Onúmero não está na lista!')
#num.pop(2)   #Renovendo
num.sort(reverse=True)   #Colocando em ordem decrescente
print(num)
print(f'Essa lista tem {len(num)} elementos.')"""

"""valores = []

valores.append(5)
valores.append(4)
valores.append(3)
valores.append(2)
valores.append(1)

for cont in range(0,5):
    valores.append(int(input('Digite um valor inteiro: ')))   #Adicionando valores através do teclado. 

#for v in valores:
for c, v in enumerate (valores):
    #print(f'{v}...', end='')
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chequei ao final da lista.')"""

x = [9, 8, 6, 5]
y = x [:]   # Fez uma cópia do X dentro do Y
y[3] = 10

print(f'Lista A: {x}')
print(f'Lista B: {y}')