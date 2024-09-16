
### Exemplo de Requisições HTTP para API de Livros e Autores

#### 1. Criar um novo livro (POST /books)
**Método:** POST  
**URL:** http://localhost:8080/books  
**Body da Requisição:**  
```json
{
  "titulo": "O Senhor dos Anéis",
  "genero": "Fantasia",
  "ano": "1954",
  "autor_id": 1
}
```

#### 2. Listar todos os livros (GET /books)
**Método:** GET  
**URL:** http://localhost:8080/books  

#### 3. Obter detalhes de um livro específico (GET /books/{id})
**Método:** GET  
**URL:** http://localhost:8080/books/1  

#### 4. Atualizar um livro (PUT /books/{id})
**Método:** PUT  
**URL:** http://localhost:8080/books/1  
**Body da Requisição:**  
```json
{
  "titulo": "O Hobbit",
  "genero": "Fantasia",
  "ano": "1937",
  "autor_id": 1
}
```

#### 5. Excluir um livro (DELETE /books/{id})
**Método:** DELETE  
**URL:** http://localhost:8080/books/1  

#### 6. Criar um novo autor (POST /authors)
**Método:** POST  
**URL:** http://localhost:8080/authors  
**Body da Requisição:**  
```json
{
  "nome": "J.R.R. Tolkien",
  "nascimento": "1892-01-03",
  "nacionalidade": "Britânico"
}
```

#### 7. Listar todos os autores (GET /authors)
**Método:** GET  
**URL:** http://localhost:8080/authors  

#### 8. Obter detalhes de um autor específico (GET /authors/{id})
**Método:** GET  
**URL:** http://localhost:8080/authors/1  

#### 9. Atualizar um autor (PUT /authors/{id})
**Método:** PUT  
**URL:** http://localhost:8080/authors/1  
**Body da Requisição:**  
```json
{
  "nome": "J.R.R. Tolkien",
  "nascimento": "1892-01-03",
  "nacionalidade": "Britânico"
}
```

#### 10. Excluir um autor (DELETE /authors/{id})
**Método:** DELETE  
**URL:** http://localhost:8080/authors/1  
