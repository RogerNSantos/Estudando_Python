""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela. """

lista = list ()
for c in range (0, 5):   #Fazendo uma contagem de 0 a 5
    numero = int(input('Digite um valore: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionando ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):   #LEN vai contar os números da lista
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('*=' * 20)
print(f'Os valores digitados em ordem foram {lista}')