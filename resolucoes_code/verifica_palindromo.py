# Solicita uma palavra como entrada do usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Compara a palavra original com a invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
