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

galera = [['Rogério', 37], ['Santos', 28], ['Neves', 18]]
print(galera)
print(galera[2][0])

