class Livro:
  def __init__(self, titulo, genero = 'Geral', ano = None, autor_id = None):
    self.titulo = titulo 
    self.genero = genero
    self.ano = ano
    self.autor_id = autor_id
  
  def to_dict(self, livro_id):
        return {
            'id': livro_id,
            'titulo': self.titulo,
            'genero': self.genero,
            'ano': self.ano,
            'autor_id': self.autor_id
        }