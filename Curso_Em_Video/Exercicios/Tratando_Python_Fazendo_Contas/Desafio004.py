# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivos
# e todas as informações possíveis sobre ele.

x = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(x))
print("Só tem espaços? ", x.isspace())
print("É um número? ", x.isnumeric())
print("É alfabético? ", x.isalpha())
print("É alfanuérico? ", x.isalnum())
print("Está em caixa alta? ", x.isupper())
print("Está em minúscula? ", x.islower())
print("Está captalizada (Inicial maiúscula)? ", x.istitle())