#duas formas diferentes de ler arquivos


try:
    arquivo = open('emails.txt')
    print(arquivo.readlines())

    print()
    arquivo = open('emails.txt')
    for linha in arquivo:
        print(linha.strip())                #strip limpa a impressão

    print()
    print()
except FileNotFoundError:
    print('Arquivo não existe')

try:
    with open('emails.txt') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('Arquivo não encontrado')













#print(type(arquivo))                #<class '_io.TextIOWrapper'>, io = 'input output arquivo', 'TextIOWrapper arquivo de texto'

#print(arquivo)