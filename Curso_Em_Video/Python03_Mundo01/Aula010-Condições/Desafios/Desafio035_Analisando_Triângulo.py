""" Desanvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. """

print("*" * 30)
print("  Analisador de triângulos")
print("*" * 30)
ret1 = float(input("Informe o primeiro seguimento: "))
ret2 = float(input("Informe o segundo seguimento: "))
ret3 = float(input("Informe o terceiro seguimento: "))
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print("Os seguimentos podem formar um triângulo!")
else:
    print("Os seguimentos não podem formar um triangulo!")
