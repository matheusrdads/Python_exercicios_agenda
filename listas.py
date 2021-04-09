
nome = "matheus"
idade = 32

minha_lista = ["bairro", "cidade", "pais", nome, idade]    #criando a lista

minha_lista[1] = "local"                                   #substituindo itens da lista

minha_lista.append("nacionalidade")                        #adicionando itens a lista

print(minha_lista)

for item in minha_lista:                                   #para cada item imprima item
    print(item)

print(minha_lista[2])                                       #imprimindo posição 2

print(nome[2:5])                                            #strings funcionam como listas (imprimindo litras ente a posição 2 e 5)

for letra in nome:                                          #for em strings
    print(letra)