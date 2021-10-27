class Pessoa:
    def __init__(self, nome, idade, sexo, cidade, estado):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.estado = estado
    
    def mostrarinfos(self):
        print(self.nome, self.idade, self.sexo, self.cidade, self.estado)

    


pessoa_nome = input("Digite o seu nome: ")
pessoa_idade = input("Digite sua idade: ")
pessoa_sexo = input("Digite seu sexo: ")
pessoa_cidade = input("Digite sua cidade: ")
pessoa_estado = input("Digite seu estado: ")

P1 = Pessoa(pessoa_nome, pessoa_idade, pessoa_sexo, pessoa_cidade, pessoa_estado)
