# Importar banco de dados
import sqlite3

# Criar e conectar com o banco de dados que acabamos de criar
conexao = sqlite3.connect('meu_banco_de_dados.db')

# Criar tabela no banco de dados
cursor = conexao.cursor()

# Exemplo de bloco de código para criar tabela CLIENTE dentro do banco de dados "meu_banco_de_dados"
# Não se esqueça de comentar esse bloco depois de executa-lo para não ocorrer o erro de "already exists"

cursor.execute('''CREATE TABLE CLIENTE
                  (id INT PRIMARY KEY     NOT NULL,
                  nome           TEXT    NOT NULL,
                  idade            INT     NOT NULL,
                  price             DECIMAL  NOT NULL);''')

# Exemplo de bloco de código para adicionar dados ao banco
# Não se esqueça de comentar esse bloco depois de executa-lo para não ocorrer o erro de "already exists"
cursor.execute("INSERT INTO CLIENTE (id, nome, idade, price) VALUES (1, 'Amanda', 40, 200.99)")
cursor.execute("INSERT INTO CLIENTE (id, nome, idade, price) VALUES (2, 'Jão', 29, 10.15)")
cursor.execute("INSERT INTO CLIENTE (id, nome, idade, price) VALUES (3, 'Andreia', 15, 17.99)")
cursor.execute("INSERT INTO CLIENTE (id, nome, idade, price) VALUES (4, 'Bianca', 31, 300.99)")
cursor.execute("INSERT INTO CLIENTE (id, nome, idade, price) VALUES (5, 'Marcos', 45, 17.99)")

# Realizar a atualização/commit das informações inseridas no banco de dados
conexao.commit()

# Consulta simples SQL de todas as colunos da tabela CLIENTE no banco de dados
cursor.execute('SELECT * FROM CLIENTE;')

# Encerrar conexão
conexao.close()