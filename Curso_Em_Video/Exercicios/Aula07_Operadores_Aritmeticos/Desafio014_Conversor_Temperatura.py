""" Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF"""

# Ler a temperatura digitada pelo usuário
celsius = float(input("Digite a temperatura em ºC: "))

# Variavel de conversão C para F
fahrenheit = ((9 * celsius) / 5) + 32

print("A temperatura {}ºC corresponde a {}ºF".format(celsius, fahrenheit))
