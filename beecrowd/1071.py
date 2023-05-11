x = int(input())
y = int(input())

if y < x:
    aux = x
    x = y
    y = aux - 1

soma = 0
while x < y:
    x = x + 1
    if x % 2 != 0:
        soma = soma + x
print(soma)