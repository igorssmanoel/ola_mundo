

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibe(self):
        print(f"Nome: {self.nome} idade: {self.idade}")


p1 = Pessoa("Igor", 29)
p1.exibe()
