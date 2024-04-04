import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='crudpython',
)
cursor = conexao.cursor()

# CRUD
#Create
nome_produto = str(input('Qual o nome do produto que deseja adicionar ?'))
valor = int(input('Qual o valor do produto ?'))
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#Read - Ler todos os dados presente no banco de dados
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#Update - Edita os dados do banco de dados
op = str(input('Qual informação deseja alterar ?'))#operação que o cliente deseja realizar
if op == 'nome':
    id = int(input('Qual id do produto que deseja alterar o nome ?'))
    nome_produto = str(input('Qual nome deseja colocar ?'))
    comando = f'UPDATE vendas SET nome_produto = "{nome_produto}" WHERE idVendas = {id}'
    cursor.execute(comando)
    conexao.commit()
elif op == 'valor':
    id = int(input('Qual id do produto que deseja alterar o valor ?'))
    valor = int(input('Qual o valor deseja colocar ?'))
    comando = f'UPDATE vendas SET valor = {valor} WHERE idVendas = {id}'
    cursor.execute(comando)
    conexao.commit()

#Delete - Delete um dado do banco de dados
id = int(input('Qual o id do produto que deseja deletar ?'))
controle = str(input('Tem certeza que deseja deletar esse item ? [S/N]')).upper() #controle de segurança para usuário
if controle == 'S':
    comando = f'DELETE FROM vendas WHERE idVendas = {id}'
    cursor.execute(comando)
    conexao.commit()
elif controle == 'N':
    print('Operação cancelada!')

cursor.close()
conexao.close()