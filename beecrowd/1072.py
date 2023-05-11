n = int(input())

dentro = 0
fora = 0

valor_minimo = 10
valor_maximo = 20

# Escrever meu codigo

i = 0
while i < n:
    numero = int(input())
    if ((numero >= valor_minimo) and (numero <= valor_maximo)):
        dentro = dentro + 1
    else:
        fora = fora + 1
    i = i + 1

#saida
print(f"{dentro} in")
print(f"{fora} out")

