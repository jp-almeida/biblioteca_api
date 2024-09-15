from Livro import Livro

class Biblioteca:
  def __init__(self) -> None:
    self.livros = {}
    self.autores = {}
    self.proximo_id_livro = 1
    self.proximo_id_autor = 1

  def adicionarLivro(self, titulo, genero='Geral', ano=None, autor_id=None):
    livro = Livro(titulo, genero, ano, autor_id)
    livro_id = self.proximo_id_livro

    self.livros[livro_id] = livro
    self.proximo_id_livro += 1
  
  def listarLivros(self):
    resultado = []
    for livro_id, livro in self.livros.items():
      resultado.append(livro.to_dict(livro_id))
    return resultado

  def detalhesLivro(self, livro_id):
    livro = self.livros[livro_id]
    return livro.to_dict(livro_id)
  
  def atualizarLivro(self, livro_id, titulo=None, genero=None, ano=None, autor_id=None):
    livro = self.livros.get(livro_id)
    if livro:
        if titulo:
            livro.titulo = titulo
        if genero:
            livro.genero = genero
        if ano:
            livro.ano = ano
        if autor_id:
            livro.autor_id = autor_id
        return livro
    return None

b = Biblioteca()
b.adicionarLivro('1984')
b.adicionarLivro('Maquiavel')
b.adicionarLivro('Harry Potter')

print(b.atualizarLivro(3, 'Senhor dos Anéis', 'Ficção', '1999'))
print(b.detalhesLivro(3))