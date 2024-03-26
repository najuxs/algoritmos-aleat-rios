print("---------------------------")
print("---------VOTAÇÃO-----------")
print("---------------------------")

def calcular_percentual(valor, total):
    if total == 0:
        return 0
    else:
        return (valor / total) * 100

    print("Por favor, informe a quantidade de votos para cada candidato, votos nulos e votos em branco")