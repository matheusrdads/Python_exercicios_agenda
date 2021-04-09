while True:
    try:
        a = float(input('Digide o primeiro numero: '))       # essa operação poderá causasar um ValueError
        b = float(input('Digide o segundo numero: '))        # essa operação poderá causasar um ValueError

        print(a/b)                                           # essa operação poderá causasar um ZeroDivisionError
        print()

    except ValueError as error:                              # tratando erros esperados
        print('input inválido digite apenas numeros')
        print()
    except ZeroDivisionError as error:                       # tratando erros esperados
        print('Não pode ser feita divisão por Zero')
        print()
    except Exception as error:                               # tratando erros genericos
        print('Algum erro ocorreu')
        print(error)
        print()
    finally:
        print("Final do programa")