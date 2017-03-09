import sqlite3, time

###metodos

def conectar_db(db_name):
    conectar = sqlite3.connect(db_name + '.db')
    #...

def criar_db(new_db_name):
    new_db_name = str(input('Insira o nome do banco: \n'))
    c.execute('CREATE TABLE '+new_db_name+'(nome text, telefone varchar, email text, data text)')

def insert_db(n,t,e):
    d = time.strftime('%d /%m /%Y')
    c.execute('INSERT INTO '+insert_table+' VALUES(?,?,?,?)',(n,t,e,d))
    conectar.commit()

def listar(p):
    sql = 'SELECT * FROM '+insert_table
    c.execute(sql,(p,))
    print(c)

####iniciando programa



try:
    insert_name = str(input('Insira o nome do banco: \n'))
    conectar = sqlite3.connect(insert_name + '.db')
    c = conectar.cursor()

    insert_table = str(input('Insira o nome da tabela: '))
    print(' \n')

except:
    print('Houve algum erro ao logar no banco, tente novamente')
    print()
else:
    print('Conectado!\n')

try:
    dd ='s'
    criar_db(dd)
except:
    print('O Banco de Dados não foi criado\n')
else:
    print('Banco criado com sucesso\n')

try:
    print('Cadastro')
    time.sleep(1)
    n = str(input('Digite um nome: \n'))
    t = int(input('Digite um telefone: \n'))
    e = str(input('Digite um e-mail: \n'))
    insert_db(n,t,e)
except:
    print('Erro ao cadastrar\n')
else:
    print('Cadastrado com sucesso\n')