#Difetente da list e tupla o dicionário não possui indices e sim estrutura chave e valor
#Não é executado na ordem das chaves

pessoas = {
    "matheus": 20,
    "joão": 40,
    "priscila": "advogada"
}

print(pessoas)

for pessoa in pessoas.values():  # percorrendo os valores
    print(pessoa)

for pessoa in pessoas.values():  # percorrendo os valores (outro método)
    print(pessoas[pessoa])       # usando o indice que foi nomeado de pessoa

for pessoa in pessoas:           #percorrendo as chaves
    print(pessoa)