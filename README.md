# Projeto Biblioteca - Documentação

## Descrição
Este é um projeto simples que implementa uma API para gerenciar livros e autores de uma biblioteca. A API é capaz de processar requisições HTTP para operações CRUD (Criar, Ler, Atualizar e Excluir) sobre livros e autores, além de permitir a associação de livros a autores. Nossa API foi implementada usando bibliotecas nativas do Python e manipulação de sockets.

## Estrutura de Classes

O projeto é composto por quatro classes principais:

### 1. Main
Classe responsável por iniciar o servidor.
- Invoca o método `servidorBiblioteca()` da classe **Biblioteca** para começar a ouvir requisições HTTP.

### 2. Livro
Representa um livro na biblioteca.

#### Atributos:
- `titulo`: título do livro.
- `genero`: gênero do livro (opcional, valor padrão "Geral").
- `ano`: ano de publicação do livro (opcional).
- `autor_id`: ID do autor (opcional).

#### Métodos:
- `to_dict()`: converte o objeto livro para um dicionário, útil para serialização.

### 3. Autor
Representa um autor.

#### Atributos:
- `nome`: nome do autor.
- `nascimento`: data de nascimento do autor.
- `nacionalidade`: nacionalidade do autor.

#### Métodos:
- `to_dict()`: converte o objeto autor para um dicionário.

### 4. Biblioteca
Gerencia a coleção de livros e autores e as associações entre eles.

#### Atributos:
- `livros`: dicionário que armazena livros, com o ID do livro como chave.
- `autores`: dicionário que armazena autores, com o ID do autor como chave.
- `associacoes`: dicionário que associa autores a livros.
- `proximo_id_livro`: ID a ser atribuído ao próximo livro adicionado.
- `proximo_id_autor`: ID a ser atribuído ao próximo autor adicionado.
