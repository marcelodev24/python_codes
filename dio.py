
def Equilibrando_o_Saldo():
    saldoAtual = float(input('saldoAtual: '))
    valorDeposito = float(input('valorDeposito: '))
    valorRetirada = float(input('valorRetirada: '))
    saldo = saldoAtual
    saldo+=valorDeposito
    if saldoAtual >= valorRetirada:
        saldo -= valorRetirada

    print(f'Saldo atualizado na conta: {saldo:.1f}')



def Juros_Compostos():
    valorInicial = float(input('valorInicial: '))
    taxaJuros = float(input('taxaJuros: '))
    periodo = float(input('periodo: '))

    valorFinal = valorInicial * (1+taxaJuros)**periodo

    print(f'{valorFinal:.2f}')

def Condicionalmente_Rico():
    saldoTotal = int(input('saldoTotal: '))
    valorSaque = int(input('valorSaque: '))

    if valorSaque <= saldoTotal:
        valor = saldoTotal - valorSaque
        print(f'Saque realizado com sucesso. Novo saldo: {valor}')
    else:
        print(f"Saldo insuficiente. Saque nao realizado!")

Condicionalmente_Rico()