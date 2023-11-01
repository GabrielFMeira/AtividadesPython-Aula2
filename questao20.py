compras = []

for i in range(60):
    precoCompra = float(input("Insira o preço do produto ou digite 0 para finalizar: "))

    if precoCompra == 0:

        troco = float(input("Insira o valor para troco: "))
        print("========================================")
        print("LOJAS TABAJARA")
        print("Compra Finalizada!")

        numeroItem = 1

        for valor in compras:

            print ("Valor Item", numeroItem, ": R$", valor)
            numeroItem+=1

        print("Valor Total: R$", sum(compras))
        print("Troco: R$", troco-sum(compras))

        print("========================================")

        break

    else:

        compras.append(precoCompra)
        i+=1