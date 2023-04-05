linha1 = input().split()


c1 = int(linha1[0])
qtd1 = int(linha1[1])
v1 = float(linha1[2])

linha2 = input().split()

c2 = int(linha2[0])
qtd2 = int(linha2[1])
v2 = float(linha2[2])

resultado = qtd1 *v1 + qtd2* v2

print(f"VALOR A PAGAR: R$ {resultado:.2f}")
