"""teste = list ()
teste.append('Rogério')   #Adicionando nome
teste.append(37)   #Adicipnando idade
#print(teste)

galera = list ()
galera.append(teste[:])   #Fazendo uma cópia da lista teste
teste[0] = 'Santos'
teste[1] = 28
galera.append(teste[:])
print(galera)"""

"""galera = [['Rogério', 37], ['Santos', 28], ['Neves', 18]]
print(galera)
print(galera[0][1])
for p in galera:
    print(p)
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')
"""

galera = list ()
dado = list()
totalmaior = totalmenor = 0
for c in range (0, 4):
    dado.append(str(input('Seu nome: ')))
    dado.append(int(input('Sua idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} menor de idade.')
        totalmenor += 1
        
print(f'Temos {totalmaior} maior de idade e {totalmenor} menor de idade.')   
