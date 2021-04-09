try:
    with open('emails.txt') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print("Arquivo não encontrado")


'''
'r' abre para ler
'w' abre para escrever / o arqui é sobre escrito 
'a' abre para ler / novo conteúdo será adicionado ao final do arquivo


>>>>>>>>exemplos de Outros Modos>>>>>>>>>>>
'r+' abre para ler e escrever / porem se o arquivo não existir não será criado
'+' acrescenta outras funcionalidades em modos existentes
'b' arquivos binarios

'''

