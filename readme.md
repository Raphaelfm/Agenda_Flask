### Fiz esse projeto para ajudar uma amiga que está em formação na mesma faculdade onde estudo, visando ajudar.
### Esse projeto é uma agenda telefônica web, desenvolvida com python com o framework flask.
### Tecnologias:
Python, mysql, html5, css3.


# Pacotes Necessários
### Rode em seu console, no vscode ou no cmd(Prompt de comando)

## Flask
pip install Flask

## mysql-connector-python
pip install mysql-connector-python


# Banco de Dados
Crie um banco no mysql, no meu caso criei um banco chamado mydatebase:
## Comando para criar o banco de dados:
create database mydatabase

## Comando para criar a tabela usuários com suas respectivas colunas:
CREATE TABLE contatos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255), telefone VARCHAR(255));


# Rodando o projeto
Abra o projeto no vscode e no terminal do vscode digite o comando: python app.py
