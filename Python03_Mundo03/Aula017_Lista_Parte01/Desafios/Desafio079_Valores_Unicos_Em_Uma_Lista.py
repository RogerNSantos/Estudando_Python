""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
únicos digitados, em ordem crescente. """

numero = list ()
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in numero:
        numero.append(n)   #Adicionando os números
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar!')
    r = str(input('Quer contibuar? [S/N] '))
    if r in 'Nn':
        break
print('-*' * 20)
numero.sort()   #Para deixar a lista em ordem
print(f'Você digitou os valores {numero}')
    