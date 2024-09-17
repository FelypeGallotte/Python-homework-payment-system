pagamento = dict(metodo=str,num_tr=int,dt_pagamento=str,notas=str)

def cadastrar_pagamento(pagamentos:list):
    pag = pagamento.copy()
    met = input("O método de pagamento é Cartão de Crédito ou Transferência bancária?  ").upper()
    #condicional para saber se precisa de numero da transação
    if met in ["SIM", "S"]:
       #perguntas caso o metodo seja credito ou transferencia 
       pag['num_tr'] = int(input('Informe o número de transação: '))
       pag['metodo'] = input('Informe se é Cartão de Crédito ou Transferência Bancária : ')
    #perguntas caso o metodo nao seja credito ou transferencia
    else:
        pag['num_tr'] = None       
        pag['metodo'] = input('Informe o método de pagamento: ')
    #perguntas finais independente do metodo de pagamento
    pag['dt_pagamento'] = input('Informe a data do pagamento : ')
    pag['notas'] = input('Informe uma nota ou comentário para o pagamento : ')
    pagamentos.append(pag)

def imprimir_pagamento(pagamentos:list):
    for pag in pagamentos:
      print(pag) 