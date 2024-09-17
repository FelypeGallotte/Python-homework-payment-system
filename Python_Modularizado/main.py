import fornecedor_function
import contas_functions
import pagamento_functions
fornecedor=list()
contas=list()
pagamentos = list()

repeticao=True
def menu():
    print("1-Cadastrar Fornecedor")
    print("2-Imprimir Fornecedor")
    print("3-Cadastrar Conta")
    print("4-Imprimir Conta")
    print("5-Cadastrar Pagamento")
    print("6-Imprimir Pagamento")



while repeticao:
    menu()
    opcao = int(input("Escolha uma opção."))
    if opcao == 1:
        fornecedor_function.cadastrar_fornecedor(fornecedor)

    elif opcao == 2:
        fornecedor_function.imprimir_fornecedor(fornecedor)

    elif opcao == 3:
        contas_functions.cadastrar_contas(contas)

    elif opcao == 4:
        contas_functions.imprimir_contas(contas)
    
    elif opcao == 5:
        pagamento_functions.cadastrar_pagamento(pagamentos)
    
    elif opcao == 6:
        pagamento_functions.imprimir_pagamento(pagamentos)

    saida = input("Deseja encerrar o programa?").upper()
    if saida in ["SIM", "S"]:
        repeticao = False

    