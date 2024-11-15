# Solicita dois números como entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe as opções de operações
print("\nEscolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita a escolha da operação
operacao = input("Digite o número correspondente à operação desejada (1/2/3/4): ")

# Realiza a operação escolhida e exibe o resultado
if operacao == '1':
    resultado = num1 + num2
    print(f"\nResultado da adição: {num1} + {num2} = {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"\nResultado da subtração: {num1} - {num2} = {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"\nResultado da multiplicação: {num1} * {num2} = {resultado}")
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado da divisão: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida.")
else:
    print("\nOpção inválida. Por favor, escolha uma operação válida (1/2/3/4).")
