#interface com estruturas para acessar e manipular o banco
import cx_Oracle 

#gera a string para conectar o banco, passando como parametros o host, a porta do db e o nome do mesmo
dsn_tns = cx_Oracle.makedsn('localhost', '1522', service_name='GDI') 
#faz a conexao com o banco
conn = cx_Oracle.connect(user=r'system', password='password', dsn=dsn_tns)
conn.autocommit = True

#cria um novo cursor para manipular o db
c = conn.cursor()

#projeta e imprime todos os dados de todos os empregados
c.execute('select * from empregado')
for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4],'-', row[5],'-', row[6])
print("")

#insere a nova empregada Lidia Gomes, e depois faz uma consulta para mostrar os dados dela
c.execute("insert into empregado (cpf, cpf_lider, nome, dt_nasc, sexo, salario, cep) values (5555, 3333, 'Lidia Gomes', to_date ('13/07/1989', 'dd/mm/yyyy'), 'F', 2500.00, 555313)")
c.execute('select * from empregado where cpf = 5555')
for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4],'-', row[5],'-', row[6])
print("")

#atualiza o salario do empregado com cpf 5555 para 5000
c.execute('update empregado set salario = 5000 where cpf = 5555')
c.execute('select * from empregado where cpf = 5555')
for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4],'-', row[5],'-', row[6])
print("")

#cria a lista contendo os dados dos empregados a serem inseridos
rows = [(6666,1111,'Joaquim Carvalho','28/04/1983','M',4500.00,138893),(7777,6666,'Paloma Morais','05/12/1990','F',3500.00,401000),]
#insere consecutivamente os empregados da lista acima e depois exibe os dados de todos os empregados na tela
c.executemany("insert into empregado (cpf, cpf_lider, nome, dt_nasc, sexo, salario, cep) values (:1,:2,:3,to_date (:4, 'dd/mm/yyyy'),:5,:6,:7)", rows)
c.execute('select * from empregado')
for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4],'-', row[5],'-', row[6])
print("")

#remove o empregado com cpf = 6666
c.execute('delete from empregado where cpf = 7777')
c.execute('select * from empregado')
for row in c:
    print (row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4],'-', row[5],'-', row[6])
print("")

#termina a conexao com o banco
conn.close()
