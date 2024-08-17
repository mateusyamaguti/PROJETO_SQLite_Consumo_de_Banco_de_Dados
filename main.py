# Importar banco de dados
import sqlite3

# Criar banco de dados teste no PowerShell
# '''.\sqlite3 meu_banco_de_dados.db'''
# '''Testar a criação no sqlite online'''

# Conectar com o banco de dados que acabamos de criar
conexao = sqlite3.connect('meu_banco_de_dados.db')

# Criar tabela no banco de dados

cursor = conexao.cursor()

# cursor.execute('''CREATE TABLE nome_da_tabela
#                   (id INT PRIMARY KEY     NOT NULL,
#                   nome           TEXT    NOT NULL,
#                   idade            INT     NOT NULL);''')

# Adicionar dados ao banco
# cursor.execute("INSERT INTO nome_da_tabela (id, nome, idade) VALUES (3, 'Amanda', 40)")

# # Consulta simples SQL
cursor.execute('SELECT * FROM nome_da_tabela;')

# # Apresentar o resultado da consulta com o comando fe
res = cursor.fetchall()
print(res)

# Retornar o resultado em apenas uma linha

for item in res:
    print(item)

# conexao.commit()


# Encerrar conexão
# conexao.close()

# conexao = sqlite3.connect('rexon_metals.db')
