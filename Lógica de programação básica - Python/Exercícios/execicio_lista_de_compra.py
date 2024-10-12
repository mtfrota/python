"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apgar e listar valores
da sua lista.
Não permita que o programa quebre com erros de
indices inexistentes na lista.


"""


lista_compras = []

def adicionar_item(lista):
    item = input("Digite o item que deseja adicionar à lista: ")
    lista.append(item)
    print(f"{item} foi adicionado à lista.")

def listar_itens(lista):
    if not lista:
        print("A lista está vazia...")
    else:
        print("itens na lista de compras: ")
        for index, item in enumerate(lista, start=1):
            print(f"{index}. {item}")

def remover(lista):
    try:
        listar_itens(lista)
        indice = int(input("Digite o número do item que deseja remover: ")) - 1
        if 0 <= indice < len(lista):
            removido = lista.pop(indice)
            print(f"{removido} foi removido da lista.")
        else:
            print("Indice inválido, tente novamente...")
    except ValueError:
        print("Por favor, digite um número válido.")

def menu():
    print("\nMenu")
    print("1. Adicionar item.")
    print("2. Listar itens.")
    print("3. Remover item.")
    print("4. Sair")

lista_compras = []

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_item(lista_compras)
    elif escolha == '2':
        listar_itens(lista_compras)
    elif escolha == '3':
        remover(lista_compras)
    elif escolha == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")


    
