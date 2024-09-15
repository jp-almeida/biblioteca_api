import itertools

class Livro:
  id_iter = itertools.count()
  def __init__(self, titulo, genero = 'Geral', ano = '2024', autor_id = None):
    self.id = next(self.id_iter)
    self.titulo = titulo 
    self.genero = genero
    self.ano = ano
    self.autor_id = autor_id