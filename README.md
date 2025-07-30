# TUTORIAL_SQLite_Consumo_de_Banco_de_Dados

> Status do Projeto: Projeto em fase de desenvolvimento

<h3>Objetivo:</h3> 
<p>
Este tutorial tem o objetivo didático de ensinar de forma prática o consumo de banco de dados por meio da linguagem de programação Python. Para tal será utlizado a biblioteca <b>SQLite</b> para efetuar a comunição e a comunicação com o banco de dados.
</p>

### Tecnologias

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


### Tópicos 

Configurações iniciais
- Importação do SQLite
- Criação de Banco de Dados
- Consultando BD no SQLite Online

Minha primeira Query
- Conectar BD com método with
- Consultar dados por meio de Query
- Manipular dados

Manipulando banco de dados
- Atualizar dados
- Excluir dados

📝 ### Descrição do Projeto – Consumo de Banco de Dados SQLite com Python
Este projeto em Python tem como objetivo demonstrar operações básicas de consumo e manipulação de dados em bancos de dados SQLite. Ele oferece uma interface simples via código para:

- Conectar a um banco de dados SQLite;
- Consultar todas as tabelas disponíveis no banco;
- Listar os dados de uma tabela específica;
- Contar o número de registros em uma tabela;
- Inserir novos registros em uma tabela existente;
- Deletar uma tabela do banco de dados.

É um ótimo exemplo educacional para quem está aprendendo sobre bancos de dados relacionais e como integrá-los a aplicações Python usando a biblioteca padrão sqlite3.

🛠️ Funcionalidades
Função	Descrição
- conectar_com_db(db_name)	Estabelece conexão com o banco db_name.db.
- consultar_tabelas_db(db_name)	Mostra todas as tabelas disponíveis no banco.
- consultar_dados_em_tabelas(db, tabela)	Lista todos os dados de uma tabela específica.
- consulta_tamanho_da_tabela(db, tabela)	Retorna o número de registros da tabela.
- inserir_dados_em_tabela(...)	Insere um novo registro com id, nome e idade em uma tabela.
- deletar_tarefa(db, tabela)	Remove a tabela indicada do banco.

▶️ ### Como Rodar a Aplicação
✅ Pré-requisitos:

- Ter o Python 3.7+ instalado.
- Ter a biblioteca padrão sqlite3 (já vem com o Python).
- Ter ou criar um arquivo .db com as tabelas adequadas (ex: alunos.db).

📦 1. Instale o Python (se ainda não tiver)
https://www.python.org/downloads/

📁 2. Estrutura esperada
Você deve ter uma base SQLite com pelo menos uma tabela compatível com este esquema, por exemplo:
```
sql
CREATE TABLE usuario (
  id INTEGER PRIMARY KEY,
  nome TEXT,
  idade INTEGER
);
```
Você pode criar isso com um gerenciador SQLite (como DB Browser for SQLite) ou via terminal Python.

💻 3. Execute o código
Salve o código em um arquivo, por exemplo: sqlite_app.py.

Edite a parte final do código, descomentando as funções desejadas. Exemplo:
```
python

consultar_tabelas_db("alunos")
inserir_dados_em_tabela("alunos", "usuario", "Tiago", 30)
consultar_dados_em_tabelas("alunos", "usuario")
```

No terminal, execute o script:
```
bash

python sqlite_app.py
```
## Desenvolvedores/Contribuintes :octocat:

Liste o time responsável pelo desenvolvimento do projeto

| [<img src="https://avatars.githubusercontent.com/u/104587996?s=400&u=3566cc0da3b05b02e8cd36bed3c709d0046f5b61&v=4" width=115><br><sub>Mateus Yamaguti</sub>](https://github.com/Diana-ops) |  
| :---: | :---: | :---: 

## Licença 

The [MIT License]() (MIT)

Copyright :copyright: Ano - Titulo do Projeto
