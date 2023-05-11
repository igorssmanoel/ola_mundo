
def le_dados():
    x = int(input("Digite o valor: "))
    porcentagem = int(input("Digite a porcentagem: "))

    return [x,porcentagem]

def calculaSalario(salario_base, porcentagem):
    resultado = salario_base + porcentagem*salario_base/100

    resultado = resultado + 200 
    return resultado

def exibe_salario(resultado):
    print(f"O salario é de {resultado}")


salario_base,porcentagem = le_dados()
resultado = calculaSalario(salario_base, porcentagem)
exibe_salario(resultado)


""" def print_hello():
    print("Hello World")

print_hello() """

