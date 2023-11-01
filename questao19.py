# Declaração das variáveis
preco_pao = float(input("Preço do pão: R$ "))
# Loop para gerar a tabela
for quantidade in range(1, 51):
    valor = quantidade * preco_pao
    print(f"{quantidade} - R$ {valor:.2f}")