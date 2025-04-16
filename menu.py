# 1.3 Implemente uma função chamada menu que ofereça as seguintes opções ao usuário:
# 1. Somar
# 2. Subtrair
# 3. Multiplicar
# 4 . Dividir
# 0. Sair


from calculadora import somar, subtrair, multiplicar, dividir


def menu():
    while True:
        print("\nEscolha uma opção:")

        print("1.somar")
        print("2.subtrair")
        print("3. multiplicar")
        print("4.divisao")
        print("0.sair")

        opcao = input("Digite uma opção:")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao in ['1', '2', '3', '4']:
            a = float(input("Digite o primeiro número:"))
            b = float(input("Digite o segundo número:"))
