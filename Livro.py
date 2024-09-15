import itertools

class Livro:
  id_iter = itertools.count()
  def __init__(self, titulo, genero, ano, autor):
    self.id = next(self.id_iter)
    self.titulo = titulo 
    self.genero = genero
    self.ano = ano
    self.autor = autor
  
  def display(self):
    print(self.id)
