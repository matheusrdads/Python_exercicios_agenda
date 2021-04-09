AGENDA = {}

AGENDA['Matheus'] = {  # adicionando item no dicionario com a chave matheus
    'numero': '999987777',
    'email': 'matheus@gmail.com',
    'endereco': 'Rua 3',
}

AGENDA['maria'] = {
    'numero': '995587777',
    'email': 'maria@gmail.com',
    'endereco': 'Rua 4',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contatos(contato)
        print('---------------')


def buscar_contatos(valor):
    try:
        if (valor):
            print('Nome:', valor)
            print('Telefone:', AGENDA[valor]['numero'])
            print('Email:', AGENDA[valor]['email'])
            print('Endereço:', AGENDA[valor]['endereco'])
        elif (valor >= 0):
            print("passe um argumento")
            print('-------------------------------------')
    except KeyError:
        print(">>>>>>>>    Contato inexistente")
    except Exception as error:
        print(error)

def incluir_editar_contato(contato, numero, email, endereco):
    AGENDA[contato] = {
        'numero': numero,
        'email': email,
        'endereco': endereco,
    }
    print()
    print('>>>>>>>>    Contato {} incluído/editado com sucesso'.format(contato))
    print()

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print()
        print('>>>>>>>>    Contato {} excluído com sucesso'.format(contato))
        print()
    except KeyError:
        print(">>>>>>>>    Contato inexistente")
    except Exception as error:
        print(error)

def exportar_contato():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('nome, telefone, email, endereco')
            for contato in AGENDA:
                numero = AGENDA[contato]['numero']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, numero, email, endereco))
        print('Agenda exportada com sucesso !')
    except Exception as error:
        print(error)

def imprimir_menu():
    print('-------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contatos da agenda')
    print('3 - Incluir contatos da agenda')
    print('4 - Editar contatos da agenda')
    print('5 - Excluir contatos da agenda')
    print('6 - Exportar arquivos para CSV')
    print('0 - Fechar agenda')
    print('-------------------------------------')

while True:
    imprimir_menu()

    opcao = input('Digite uma opção: ')    # o input sempre transforma o valor de entrada em string antes de armazenar
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contatos(contato)
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        numero = input('Digite o nome do numero: ')
        email = input('Digite o nome do email: ')
        endereco = input('Digite o nome do endereco: ')
        incluir_editar_contato(contato, numero, email, endereco)
        buscar_contatos(contato)
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contato()
    elif opcao == '0':
        print('>>>>>>>>    Fechando o Programa')
        break
    else:
        print(">>>>>>>>    Opção inválida")

