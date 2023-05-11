#ler 2 valores
#Enquanto o segundo valor for igual a 0
#ler novamente os 2 valores e mostrar as mensagens

a = int(input())
b = int(input())

while b == 0:
    print("Não é possível realizar operações com o segundo valor valendo 0")
    a = int(input())
    b = int(input())

resultado_soma = a + b
resultado_subtracao = a - b
resultado_multiplicacao = a * b
resultado_divisao = a / b

print(f"A soma de {a} + {b} = {resultado_soma}")
print(f"A subtração de {a} - {b} = {resultado_subtracao}")
print(f"A multiplicação de {a} * {b} = {resultado_multiplicacao}")
print(f"A divisão de {a} / {b} = {resultado_divisao}")

