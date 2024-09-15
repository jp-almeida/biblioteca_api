import itertools

class Autor:
    def __init__(self, nome, nascimento, nacionalidade):
        self.id = next(self.id_iter)
        self.nome = nome
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade

    def insert(self, autores:dict):
        autores[self.id] = self

    def details(self):
        print(f'ID: {self.id}')
        print(f'Nome: {self.nome}')
        print(f'Data de nascimento:  {self.nascimento}')
        print(f'Nacionalidade: {self.nacionalidade}')