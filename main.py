# Lista com 15 nomes
nomes = ['Alex', "joâo", "Monyelle", 'Carlos', 'Tiago', 'Marcos','Elaine','Luiz','Brenda','Leandro', 'Leonardo','Artur','Valderval','Walker','Karina']

# usuário informa o nome a ser pesquisado

nome = input('informe o nome a ser perquisado: \n').capitalize()

# verificar se o nome está na lista 



try:
    # pequisa do indice
    indice = nomes.index(nome)
    print(f'O nome {nome} está na lista localizado no índice {indice}')
except:
    print(f'O nome {nome} NÃO está na lista!!!!')