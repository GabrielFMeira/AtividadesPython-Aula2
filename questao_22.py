##Inicializando as variaveis para contar os votos
votos_candidato =[0,0,0,0]
votos_nulos = 0
votos_branco = 0
total_votos = 0

# Mapeando os votos para os nomes dos candidatos 
candidatos = {
    1: "Jose",
    2: "Joao",
    3: "Maria",
    4: "Ana"
}

# Recebendo os votos 
numero_eleitores = int(input(" Digite o numero de eleitores: "))
i = 0
for i in range(numero_eleitores):
    voto = int(input(" Digite o codigo do voto (1 a 4 para os candidatos, 5 para nulo, 6 para branco e 0 para cancelar)"))
    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos_candidato[voto -1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Codigo invalido")
else: 
#calculando o total de votos
    total_votos = sum(votos_candidato) + votos_nulos + votos_branco

#Resultados
    print(" Resultado da eleicao: ")
    for i in range(4):
        print(f"{candidatos[i+1]}: {votos_candidato[i]} votos ({(votos_candidato[i] / total_votos) * 100:.2f}%)")

    print(f"Votos nulos: {votos_nulos} votos ({(votos_nulos / total_votos) * 100:.2f}%)")
    print(f"Votos em branco: {votos_branco} votos ({(votos_branco/total_votos) * 100:.2f}%)")
    print(f"Total de votos: {total_votos}")