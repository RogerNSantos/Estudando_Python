""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a BASE DE CONVERSAÃO
 - 1 para BINÁRIPO
 - 2 para OCTAL
 - 3 para HEXADECIMAL """

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL. """)

opcao = int(input("Informe sua opção: "))
if opcao == 1:
    print("Número {} convertido para BINÁRIO é {} ".format(num, bin(num)[2:]))
elif opcao == 2:
    print("Número {} convertido para OCTAL é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("Número {} convertido para HEXADECIMAL é {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida. Tente novamente.")