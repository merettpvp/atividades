# Esta função recebe uma lista de números e retorna a média.
def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Chamando a função para calcular a média de uma lista de números.
lista_numeros = [10, 20, 30, 40, 50]
media_resultante = calcular_media(lista_numeros)
print(f"A média dos números na lista é {media_resultante}")