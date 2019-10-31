#interface com estruturas para acessar e manipular o banco
import cx_Oracle

def take_cursor():
    # gera a string para conectar o banco, passando como parametros o host, a porta do db e o nome do mesmo
    dsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='GDI')
    # faz a conexao com o banco
    conn = cx_Oracle.connect(user=r'system', password='password', dsn=dsn_tns)
    conn.autocommit = True

    # cria um novo cursor para manipular o db
    return conn.cursor()


def insert(table):
    c = take_cursor()
    c.execute("insert into "
              + table +
              " (cpf, cpf_lider, nome, dt_nasc, sexo, salario, cep) values (5555, 3333, 'Lidia Gomes', to_date ('13/07/1989', 'dd/mm/yyyy'), 'F', 2500.00, 555313)")


def select(table, filter_column, filter):
    c = take_cursor()
    c.execute('select * from ' + table + ' where ' + filter_column + ' = ' + filter)
    for row in c:
        print (row)


def update(table, column, filter_column, filter, new_value):
    c = take_cursor()
    c.execute('update ' + table + ' set ' + column + ' = ' + new_value + ' where ' + filter_column + ' = ' + filter)
    print('Atualizado com sucesso')

def delete(table, filter_column, filter):
    c = take_cursor()
    c.execute('delete from ' + table + ' where ' + filter_column + ' = ' + filter)
    print('Deletado com sucesso')
