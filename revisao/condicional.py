a = int(input())
b = int(input())

if b > 0:
    print("Não é possível realizar operações com o segundo valor valendo 0")
else:
    resultado_soma = a + b
    resultado_subtracao = a - b
    resultado_multiplicacao = a * b
    resultado_divisao = a / b

    print(f"A soma de {a} + {b} = {resultado_soma}")
    print(f"A subtração de {a} - {b} = {resultado_subtracao}")
    print(f"A multiplicação de {a} * {b} = {resultado_multiplicacao}")
    print(f"A divisão de {a} / {b} = {resultado_divisao}")

