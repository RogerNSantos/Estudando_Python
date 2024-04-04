""" Refaça o DESAFIO 035  doa triâbgulos, acrescentando o recurso de mostrar que tipo de triânguo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes """

print("*" * 30)
print("  Analisador de triângulos")
print("*" * 30)
ret1 = float(input("Informe o primeiro seguimento: "))
ret2 = float(input("Informe o segundo seguimento: "))
ret3 = float(input("Informe o terceiro seguimento: "))
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print("Os seguimentos podem formar um triângulo ", end = "")
    if ret1 == ret2 == ret3:
        print("EQUILÁTERO!")
    elif ret1 != ret2 != ret3 != ret1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")

else:
    print("Os seguimentos não podem formar um triangulo!")