# Solicita um número inteiro como entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar usando a operação módulo
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
