
import sqlite3


# Conexão com banco
def conectar_com_db(db_name):
    with sqlite3.connect(f'{db_name}.db') as conexao:
        cursor = conexao.cursor()
        return cursor

# Consultar quais tabelas existem em banco de dados
def consultar_tabelas_db(db_name):
    cursor = conectar_com_db(db_name)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    res = cursor.fetchall()
    for item in res:
        print(item)

# Consultar todos os dados na tabela
def consultar_dados_em_tabelas(db_name, table_name):
    cursor = conectar_com_db(db_name)
    cursor.execute(f"SELECT * FROM {table_name};")
    res = cursor.fetchall()
    for item in res:
        print(item)

# Consultar o tamnho da tabela
def consulta_tamanho_da_tabela(db_name, table_name):
    cursor = conectar_com_db(db_name)
    cursor.execute(f"SELECT COUNT (*) FROM {table_name};")
    res = cursor.fetchall()
    return(res[0][0])

# Inserir dados em uma tabela
def inserir_dados_em_tabela(db_name, table_name, name, idade):
    cursor = conectar_com_db(db_name)
    id = consulta_tamanho_da_tabela(db_name, table_name)+1
    print(id)
    cursor.execute(f"INSERT INTO {table_name} (id, nome, idade) VALUES ({id}, '{name}', {idade})")
    cursor.connection.commit()

# Deletar um tabela
def deletar_tarefa(db_name, table_name):
    cursor = conectar_com_db(db_name)
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

## Descomente as funções abaixo para poder utiliza-las

# consultar_tabelas_db("alunos")
# consultar_dados_em_tabelas("rexon_metals", "CUSTOMER")
# print(consulta_tamanho_da_tabela("rexon_metals", "CUSTOMER"))
# inserir_dados_em_tabela('alunos', 'usuario', 'Tiago', 30)
# consultar_dados_em_tabelas("alunos", "usuario")
# deletar_tarefa("alunos", 'nome_da_tabela')

