#processo de cadastramento do usuário
fornecedores = dict(nome=str, endereco=str, telefone=int, info_contatos=str)
fornecedor=list()
cadastrando=True
while cadastrando:
    forn = fornecedores.copy()
    forn['nome'] = input('Informe seu nome: ')
    forn['endereco'] = input('Informe seu endereço: ')
    try:
        forn['telefone'] = int(input('Informe seu telefone : '))
    except ValueError:
        print('Digite um número válido.')
        continue
    forn['info_contatos'] = input('Informe suas informações de contato: ')
    fornecedor.append(forn)
    saida = input("Deseja encerrar o cadastro?").upper()
    if saida in ["SIM", "S"]:
        cadastrando = False
        #break
#processo de informação do fornecedor
for forn in fornecedor:
    print(forn)
    
conta = dict(numero_fatura=int, data_emissao=str, data_vencimento=str, valor_fatura=float, descricao_fatura=str, forn_associado=forn['nome'], status_pagamento=str)
contas=list()    
cadastrando = True
while cadastrando:
    cont = conta.copy()
    cont['forn_associado'] = input('Informe o fornecedor associado: ')
    if cont['forn_associado'] != forn['nome']:
        print("Fornecedor inválido.")
        continue 
    else:
        try:
            cont['numero_fatura'] = int(input('Informe seu número da fatura: '))
            cont['valor_fatura'] = float(input('Informe o valor da fatura: '))
        except ValueError:
            print('Digite um número válido.')
            continue
        cont['data_emissao'] = input('Informe a data de emissão: ')
        cont['data_vencimento'] = input('Informe a data de vencimento : ')
        cont['descricao_fatura'] = input('Informe a descrição da fatura: ')
        cont['status_pagamento'] = input('Informe o status do pagamento [Pendente/Pago/Atrasado]: ')
        contas.append(cont)
        saida = input("Deseja encerrar o cadastro?").upper()
        if saida in ["SIM", "S"]:
           cadastrando = False
           #break 
#processo de informação das contas
for cont in contas:
     print(cont) 
     
pagamento = dict(metodo=str,num_tr=int,dt_pagamento=str,notas=str)
pagamentos = list()
registrando = True
while registrando:
    pag = pagamento.copy()
    met = input("O método de pagamento é Cartão de Crédito ou Transferência bancária?  ").upper()
    #condicional para saber se precisa de numero da transação
    if met in ["SIM", "S"]:
       #perguntas caso o metodo seja credito ou transferencia
       try:
           pag['num_tr'] = int(input('Informe o número de transação: '))
       except ValueError:
           print("Digite um número válido.")
           continue
       pag['metodo'] = input('Informe se é Cartão de Crédito ou Transferência Bancária : ')
    #perguntas caso o metodo nao seja credito ou transferencia
    else:
        pag['num_tr'] = None       
        pag['metodo'] = input('Informe o método de pagamento: ')
    #perguntas finais independente do metodo de pagamento
    pag['dt_pagamento'] = input('Informe a data do pagamento : ')
    pag['notas'] = input('Informe uma nota ou comentário para o pagamento : ')
    pagamentos.append(pag)
    saida = input("Deseja encerrar o registro?").upper()
    if saida in ["SIM", "S"]:
           registrando = False 
           #break
#processo de informação dos pagamentos
for pag in pagamentos:
    print(pag)  
print('Volte sempre!')        