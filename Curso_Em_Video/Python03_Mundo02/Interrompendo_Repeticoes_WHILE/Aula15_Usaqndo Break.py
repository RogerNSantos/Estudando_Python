num = som = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    som += num
#print('A soma vale {}'.format(som))
print(f'A soma vale {som}')