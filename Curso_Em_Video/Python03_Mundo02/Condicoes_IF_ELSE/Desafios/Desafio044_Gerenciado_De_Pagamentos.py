""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e
 CONDIÇÃO DE PAGAMENTO:
  - Á vista DINHEIRO/CHEQUE: 10% de desconto
  - Á vista no cartão:5% de desconto
  - Em até 2x no CARTÃO DE CRÉDITO: preço normal
  - 3x OU MAIS no CARTÃO DE CRÉDITO: 20% de juros """

print("\033[4;30;43m{:=^40} \033[m".format(" Lojas Python"))

preco = float(input("\nValor das compras R$ "))
print("""\033[4;30;44m ====== OPÇÕES DE PAGAMENTOS ======\033[m
[ 1 ] -> à vista dinheiro/pix.
[ 2 ] -> à vista débito.
[ 3 ] -> 2x no crtão crédito.
[ 4 ] -> 3x ou mais no cartão de crédito.""")
opcao = int(input("\033[4;30;44m======Qual a forma de pagamento? ====== \033[m"))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print("Sua compra de R$ {} com 10% de desconto vai custar {}".format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print("Sua compra de R$ {} com 5% de desconto vai custar {}".format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra de R$ {} séra parcelada em 2x de R$ {:.2f} sem juros.".format(preco, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input("Quantas parcelas? "))
    parcela = total / totalParcelas
    print("Sua compra de R$ {} será parcela em {}x de R$ {:.2f} com 20% de juros.".format(preco, totalParcelas, parcela))
else:
    total = preco
    print("\n\033[4;30;41m Opção de pagamento invalida. Tente novamente.\033[m")
#print("Sua compra de {:.2f} vai custar R$ {} no final.".format(preco, total))


