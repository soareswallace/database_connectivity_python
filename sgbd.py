#interface com estruturas para acessar e manipular o banco
import cx_Oracle
conn = cx_Oracle.connect(user=r'system', password='password', dsn=dsn_tns)

def take_cursor():
    # gera a string para conectar o banco, passando como parametros o host, a porta do db e o nome do mesmo
    dsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='GDI')
    # faz a conexao com o banco
    conn.autocommit = True

    # cria um novo cursor para manipular o db
    return conn.cursor()


def insert(sql):
    c = take_cursor()
    c.execute(sql)
    conn.close()
    print('Inserido com sucesso')


def update(sql):
    c = take_cursor()
    c.execute(sql)
    conn.close()
    print('Atualizado com sucesso')


def delete(sql):
    c = take_cursor()
    c.execute(sql)
    conn.close()
    print('Deletado com sucesso')


def select(table, filter_column, filter):
    c = take_cursor()
    c.execute('select * from ' + table + ' where ' + filter_column + ' = ' + filter)
    for row in c:
        print (row)

    conn.close()