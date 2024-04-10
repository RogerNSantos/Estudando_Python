""" Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
 Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]  # STRIP eliminado os espeços em branco, UPPER deixando tudo em maiúsculo e[0] pegando só a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, infor,e seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
