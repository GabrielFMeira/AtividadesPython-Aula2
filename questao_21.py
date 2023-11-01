# Declaração das variáveis
altura_max = 0
altura_min = 9999
peso_max = 0
peso_min = 9999
media_altura = 0
media_peso = 0
qtd_clientes = 0

# Loop para ler os dados dos clientes
while True:
    # Leitura do código do cliente
    codigo = int(input("Código do cliente: "))

    # Verificação para encerrar o programa
    if codigo == 0:
        break

    # Leitura da altura do cliente
    altura = float(input("Altura do cliente (em metros): "))

    # Leitura do peso do cliente
    peso = float(input("Peso do cliente (em kg): "))

    # Atualização das variáveis
    if altura > altura_max:
        altura_max = altura
        codigo_altura_max = codigo
    if altura < altura_min:
        altura_min = altura
        codigo_altura_min = codigo
    if peso > peso_max:
        peso_max = peso
        codigo_peso_max = codigo
    if peso < peso_min:
        peso_min = peso
        codigo_peso_min = codigo

    # Atualização da média das alturas
    media_altura += altura
    media_peso += peso
    qtd_clientes += 1

# Cálculo da média das alturas e dos pesos
media_altura /= qtd_clientes
media_peso /= qtd_clientes

# Exibição dos resultados
print("Cliente mais alto:", codigo_altura_max, altura_max)
print("Cliente mais baixo:", codigo_altura_min, altura_min)
print("Cliente mais gordo:", codigo_peso_max, peso_max)
print("Cliente mais magro:", codigo_peso_min, peso_min)
print("Média das alturas:", media_altura)
print("Média dos pesos:", media_peso)