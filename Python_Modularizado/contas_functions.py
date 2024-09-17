conta = dict(numero_fatura=int, data_emissao=str, data_vencimento=str, valor_fatura=float, descricao_fatura=str, forn_associado=str, status_pagamento=str)

def cadastrar_contas(contas:list):
    cont = conta.copy()
    cont['forn_associado'] = input('Informe o fornecedor associado: ')
    cont['numero_fatura'] = int(input('Informe seu número da fatura: '))
    cont['valor_fatura'] = float(input('Informe o valor da fatura: '))
    cont['data_emissao'] = input('Informe a data de emissão: ')
    cont['data_vencimento'] = input('Informe a data de vencimento : ')
    cont['descricao_fatura'] = input('Informe a descrição da fatura: ')
    cont['status_pagamento'] = input('Informe o status do pagamento [Pendente/Pago/Atrasado]: ')
    contas.append(cont)

def imprimir_contas(contas: list):
  for cont in contas:
     print(cont) 