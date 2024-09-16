class Autor:
    def __init__(self, nome, nascimento, nacionalidade):
        self.nome = nome
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade

    def to_dict(self, autor_id):
        return {
            'id': autor_id,
            'nome': self.nome,
            'nascimento': self.nascimento,
            'nacionalidade': self.nacionalidade
        }