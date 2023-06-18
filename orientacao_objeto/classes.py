""" pessoa1 = ["igor", 29, "12938192389"]
pessoa2 = ["Bruno", 40, "5468979878"]
print(f"O nome é {pessoa1[0]} a idade é {pessoa1[1]} e o documento é {pessoa1[2]}")
print(f"O nome é {pessoa2[0]} a idade é {pessoa2[1]} e o documento é {pessoa2[2]}") """

# Criar uma classe chamada Carro com os atributos: nome, modelo, cor e ano
# E criar um método chamado buzina que imprime na tela "Buzinaa!"

class Pessoa():
    def __init__(self, idade, documento, nome = "Fulano"):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.documento = documento
    #Métodos
    def print(self):
        print(f"O nome é {self.nome} a idade é {self.idade} e o documento é {self.documento}")


pessoa1 = Pessoa( 29, "1239812938", "Igor")
pessoa1.print()


""" pessoa1.nome = "Igor"
pessoa1.idade = 29
pessoa1.documento = "99999999999" """



""" print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.documento) """

