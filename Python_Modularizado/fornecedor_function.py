fornecedores = dict(nome=str, endereco=str, telefone=int, info_contatos=str)


def cadastrar_fornecedor(fornecedor:list):
    forn = fornecedores.copy()
    forn['nome'] = input('Informe seu nome: ')
    forn['endereco'] = input('Informe seu endereço: ')
    forn['telefone'] = int(input('Informe seu telefone : '))  
    forn['info_contatos'] = input('Informe suas informações de contato: ')
    fornecedor.append(forn)

def imprimir_fornecedor(fornecedor:list):
    for forn in fornecedor:
      print(forn)

