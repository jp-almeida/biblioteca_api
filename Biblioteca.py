from Livro import Livro
from Autor import Autor
import socket
import json 


class Biblioteca:
  def __init__(self) -> None:
    self.livros = {}
    self.autores = {}
    self.associacoes = {}
    self.proximo_id_livro = 1
    self.proximo_id_autor = 1

  #métodos para autores

  def adicionarAutor(self, nome, nascimento='Não disponível', nacionalidade = "Não disponível"):
    autor = Autor(nome, nascimento, nacionalidade)
    autor_id = self.proximo_id_autor

    self.autores[autor_id] = autor
    self.proximo_id_autor += 1
    return autor_id

  def listarAutores(self):
    resultado = []
    for autor_id, autor in self.autores.items():
      resultado.append(autor.to_dict(autor_id))
    return resultado
  
  def detalhesAutor(self, autor_id):
    autor = self.autores.get(autor_id, None)
    if autor:
      return autor.to_dict(autor_id)
    return None
  
  def atualizarAutor(self, autor_id, nome=None, nascimento=None, nacionalidade=None):
    autor = self.autores.get(autor_id)
    if autor:
        if nome:
            self.autores[autor_id].nome = nome
        if nascimento:
            self.autores[autor_id].nascimento = nascimento
        if nacionalidade:
            self.autores[autor_id].nacionalidade = nacionalidade
        return autor.to_dict(autor_id)
    return None
  
  def removerAutor(self, autor_id):
     #se o autor não existir, retornará None, que será tratado como 404
     return self.autores.pop(autor_id, None)
  
  #métodos para livros

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
  

  #metodos para associações
  def associarLivro(self, autor_id, livro_id):
    if self.associacoes.get(autor_id) != None:
      self.associacoes[autor_id].append(livro_id)
    else:
      self.associacoes[autor_id] = [livro_id]
    self.livros[livro_id].autor_id = autor_id
    return autor_id
  
  def listarLivrosAutor(self, autor_id):
    if self.associacoes.get(autor_id) != None:
      return self.associacoes[autor_id]
    return None
  
  def removerAssociacao(self, autor_id, livro_id):
    if self.associacoes.get(autor_id):
      if livro_id in self.associacoes[autor_id]:
        self.associacoes[autor_id].remove(livro_id)
        self.livros[livro_id].autor_id = None
        return livro_id
      return "Sem livro"
    return "Sem autor"
    

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
      
      #livros
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
      
      #Associações
      elif "/authors/" in path and "/books" in path:

        if method == 'POST':
          #capta ids do autor e do livro pelo path
          autor_id = int(path.split('/')[-3])
          livro_id = int(path.split('/')[-1])

          #realiza a associação 
          autor_id_associado = biblioteca.associarLivro(autor_id,livro_id)

          #pega os livros do autor e retorna-os 
          retorno = biblioteca.listarLivrosAutor(autor_id_associado)
          if retorno == "Sem autor":
            responseBody = json.dumps("Autor não encontrado")
          elif retorno == "Sem livro":
            responseBody = json.dumps("Livro não encontrado")
          else:
            responseBody = json.dumps(retorno)
            
          response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"

        elif  method == 'GET':
          #capta o id do autor pelo path
          autor_id = int(path.split('/')[-2])

          #busca os livros associados ao autor
          livros_autor = biblioteca.listarLivrosAutor(autor_id)
          
          retorno = []
          for livro_id in livros_autor:
            retorno.append(biblioteca.livros[livro_id].to_dict(livro_id))
          
          responseBody = json.dumps(retorno)
          response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"

        elif method == 'DELETE':
          #capta os ids do autor e do livro pelo path
          autor_id_d = int(path.split('/')[-3])
          livro_id_d = int(path.split('/')[-1])

          #desassocia o livro e retorna-o
          livro_desassociado = biblioteca.removerAssociacao(autor_id_d,livro_id_d)

          #manda o livro desassociado, se existir
          if livro_desassociado:
            responseBody = json.dumps({'id': autor_id_d, 'livro desassociado id ':livro_desassociado})
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
          else:
            response = "HTTP/1.1 404 Not Found\n\nAutor não encontrado"
      
      #autores
      elif path.startswith('/authors'):
        if method == 'POST' and path == '/authors':
          nome = body.get('nome')
          nascimento = body.get('nascimento')
          nacionalidade = body.get('nacionalidade')
          autor_id = biblioteca.adicionarAutor(nome, nascimento, nacionalidade)
          responseBody = json.dumps({'id':autor_id})
          response = f"HTTP/1.1 201 Created\nContent-Type: application/json\n\n{responseBody}"

        elif method == 'GET' and path == '/authors':
          autores =  biblioteca.listarAutores()
          responseBody = json.dumps(autores)
          response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
        
        elif method == 'GET' and path.startswith('/authors/'):
          autor_id = int(path.split('/')[-1])
          autor = biblioteca.detalhesAutor(autor_id)
          if autor:
            responseBody = json.dumps(autor)
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
          else:
            response = "HTTP/1.1 404 Not Found\n\nAutor não encontrado"
      
        elif method == 'PUT' and path.startswith('/authors/'):
          autor_id = int(path.split('/')[-1])

          # Passa os parâmetros ao método atualizarAutor
          nome = body.get('nome')
          nascimento = body.get('nascimento')
          nacionalidade = body.get('nacionalidade')

          # Atualiza o autor com os dados fornecidos
          autor = biblioteca.atualizarAutor(autor_id, nome=nome, nascimento=nascimento, nacionalidade=nacionalidade)

          if autor:
            responseBody = json.dumps(autor)
            response = f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responseBody}"
          else:
            response = "HTTP/1.1 404 Not Found\n\nAutor não encontrado"
        
        elif method == 'DELETE' and path.startswith('/authors/'):
          autor_id = int(path.split('/')[-1])
          autor_deletado = biblioteca.removerAutor(autor_id)
          if autor_deletado:
            responseBody = json.dumps({'id': autor_id})
            response = "HTTP/1.1 204 No Content\n\n"
          else:
            response = "HTTP/1.1 404 Not Found\n\nAutor não encontrado"
      


      else:
          # Se a rota não for encontrada
        response = "HTTP/1.1 404 \n\nRota não encontrada"

      # Enviar resposta ao cliente
      client_socket.sendall(response.encode('utf-8'))
      client_socket.close()