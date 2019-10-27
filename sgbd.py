#interface com estruturas para acessar e manipular o banco
import cx_Oracle
#gera a string para conectar o banco, passando como parametros o host, a porta do db e o nome do mesmo
dsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='GDI')
#faz a conexao com o banco
conn = cx_Oracle.connect(user=r'system', password='password', dsn=dsn_tns)
conn.autocommit = True