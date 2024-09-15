from Livro import Livro
import socket
import json 


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
    return livro_id
  
  def listarLivros(self):
    resultado = []
    for livro_id, livro in self.livros.items():
      resultado.append(livro.to_dict(livro_id))
    return resultado

  def detalhesLivro(self, livro_id):
    livro = self.livros.get(livro_id, None)
    if livro:
      return livro.to_dict(livro_id)
    return None
  
  def atualizarLivro(self, livro_id, titulo=None, genero=None, ano=None, autor_id=None):
    livro = self.livros.get(livro_id)
    if livro:
        if titulo:
            self.livros[livro_id].titulo = titulo
        if genero:
            self.livros[livro_id].genero = genero
        if ano:
            self.livros[livro_id].ano = ano
        if autor_id:
            self.livros[livro_id].autor_id = autor_id
        return livro.to_dict(livro_id)
    return None
  
  def removerLivro(self, livro_id):
     #se o livro não existir, retornará None, que será tratado como 404
     return self.livros.pop(livro_id, None)

  def servidorBiblioteca(self):
     biblioteca = Biblioteca()

     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server.bind(('localhost', 8080))
     server.listen(5)

     print('Servidor rodando em http://localhost:8080')

     while True:
      client_socket, client_address = server.accept()
      request = client_socket.recv(1024).decode('utf-8')
      request_line = request.splitlines()[0]
      method, path, _ = request_line.split(' ')
      
      # Extrai o corpo da requisição
      try:
        body = request.split('\r\n\r\n')[1]
        body = json.loads(body)
      except:
        body = {}
      
      #Roteamento
        
      if path.startswith('/books'):
        if method == 'POST' and path == '/books':
          titulo = body.get('titulo')
          genero = body.get('genero')
          ano = body.get('ano')
          autor_id = body.get('autor_id')
          livro_id = biblioteca.adicionarLivro(titulo, genero, ano, autor_id)
          responseBody = json.dumps({'id':livro_id})
          response = f"HTTP/1.1 201 Created\nContent-Type: application/json\n\n{responseBody}"

        elif method == 'GET' and path == '/books':
          livros =  biblioteca.listarLivros()
          responseBody = json.dumps(livros)
          response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
        
        elif method == 'GET' and path.startswith('/books/'):
          livro_id = int(path.split('/')[-1])
          livro = biblioteca.detalhesLivro(livro_id)
          if livro:
            responseBody = json.dumps(livro)
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
          else:
            response = "HTTP/1.1 404 Not Found\n\nLivro não encontrado"
      
        elif method == 'PUT' and path.startswith('/books/'):
          livro_id = int(path.split('/')[-1])

          # Passa os parâmetros ao método atualizarLivro
          titulo = body.get('titulo')
          genero = body.get('genero')
          ano = body.get('ano')
          autor_id = body.get('autor_id')

          # Atualiza o livro com os dados fornecidos
          livro = biblioteca.atualizarLivro(livro_id, titulo=titulo, genero=genero, ano=ano, autor_id=autor_id)

          if livro:
            responseBody = json.dumps(livro)
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
          else:
            response = "HTTP/1.1 404 Not Found\n\nLivro não encontrado"
        
        elif method == 'DELETE' and path.startswith('/books/'):
          livro_id = int(path.split('/')[-1])
          livro_deletado = biblioteca.removerLivro(livro_id)
          if livro_deletado:
            responseBody = json.dumps({'id': livro_id})
            response = "HTTP/1.1 204 No Content\n\n"
          else:
            response = "HTTP/1.1 404 Not Found\n\nLivro não encontrado"
        else:
            # Se a rota não for encontrada
            response = "404 \n\nRota não encontrada"

        # Enviar resposta ao cliente
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()