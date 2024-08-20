# importar biblioteca SQLite3
import sqlite3

with sqlite3.connect("rexon_metals.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    res = cursor.fetchall()


# Executar o comando SQL para listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Buscar todas as tabelas
tabelas = cursor.fetchall()
print(tabelas)

nome_da_tabela = "CUSTOMER"

# Executar o comando PRAGMA para obter informações sobre as colunas
cursor.execute(f"PRAGMA table_info({nome_da_tabela});")

# Buscar todas as colunas
colunas = cursor.fetchall()
print(colunas[0])

# contar a quantidade o tamanho da tabela
cursor.execute(f"SELECT COUNT(*) FROM {nome_da_tabela};")
res = cursor.fetchall()[0][0]
print(res)

# Manipular dados
cursor.execute("SELECT PRODUCT_ID, DESCRIPTION, PRICE, PRICE * 1.07 AS TAXED_PRICE FROM PRODUCT;")
res = cursor.fetchall()

for item in res:
    print(item)