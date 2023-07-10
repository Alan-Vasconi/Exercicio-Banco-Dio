class clientesclass:
    nome = ""
    data = ""
    cpf = ""
    endereco = ""

def menu_opcoes():
    print('╔═══════════════════════════════════╗')
    print('║ Menu de opções | Banco            ║')
    print('╠═══════════════════════════════════╣')
    print('║ 1. Extrato                        ║')
    print('║ 2. Depositar                      ║')
    print('║ 3. Sacar                          ║')
    print('║ 4. Cadastrar Usuário              ║')
    print('║ 5. Cadastrar Conta Bancária       ║')
    print('║ 6. Listar Contas Bancárias        ║')
    print('║ 0. Sair                           ║')
    print('╚═══════════════════════════════════╝')
    print()
    escolha = int(input('Digite a opção que deseja: '))
    return escolha

def relatorio(extrato,valor):
    print('╔════════════════════════════════════')
    print(f'║ Saldo na conta: R$ {valor:.2f}       ')
    print('╠════════════════════════════════════')
    print(f'{extrato}')

def depositar(valor,extrato):
    soma = float(input('Digite o valor que deseja depositar: '))
    valor += soma
    extrato += f'║ Deposito: {soma:.2f}\n'
    return valor, extrato

def criar_conta(agencia,numero,cliente):
    valor = False
    elemento = input('Digite seu cpf (Formato: 000.000.000-00): ')
    contador = 0
    while contador < len(cliente):
        if cliente[contador].cpf == elemento:
            valor = True
        contador +=1
    if valor == True:
        print(f'Conta de número: {numero} criada com sucesso!')
        return {"Agência": agencia, "Numero": numero, "Cliente": elemento}
    else:
        print('Cliente não existente')
    
def sacar(valor,contador,extrato):
    if contador < 3:
        saque = float(input('Digite o valor que deseja sacar: '))
        if saque <= 500 and saque > 0:
            if valor - saque >= 0:
                valor -=saque
                print('Saque efetuado com sucesso!')
                extrato += f'║ Saque: {saque:.2f}\n'
                contador +=1
                return valor, contador, extrato
            else:
                print('Saldo insuficiente')
                return valor, contador, extrato 
        else:
            print(f'Valor superior a 500 reais ou negativo, você perdeu uma tentativa de saque, agora apenas tem {contador} disponibilidades de saque')
            return valor, contador, extrato
    else:
        print('Você não tem mais saques para fazer hoje!')
        return valor, contador, extrato
    
def cadastrar_cliente(cpf,cliente):
    N = clientesclass()
    N.nome = input('Digite o seu nome completo separado por espaços: ')
    N.data = input('Digite a sua data de nascimento no formato XX/XX/XXXX: ')
    N.endereco = input('Digite o seu endereço (Logradouro, N°, Bairro, Cidade/Sigla Estado): ')
    N.cpf = cpf
    cliente.append(N)
    return cliente

def listar(conta):
    print(conta)

    
def main():
    valor = 100
    contador = 0
    extrato = ""
    cliente = []  
    conta = []
    numero = len(conta)  
    agencia = "0001"
    escolha = menu_opcoes()
    while escolha <= 6 and escolha > 0 :
        if escolha == 1:
            if extrato is not "":
                relatorio(extrato,valor)
            else:
                print('Não foram realizadas movimentações')
        if escolha == 2:
            valor, extrato = depositar(valor,extrato)
            print(f'Saldo em conta atualizado, atualmente tem R${valor} em sua conta')
        if escolha == 3:
            valor, contador, extrato = sacar(valor,contador,extrato)
        if escolha == 4:
            elemento = input('Digite seu cpf (Formato: 000.000.000-00): ')
            contador = 0
            while contador < len(cliente):
                if cliente[contador].cpf == elemento:
                    print('CPF já cadastrado!')
                    break
                contador +=1
            else:
                cadastrar_cliente(cpf=elemento,cliente=cliente)
        if escolha == 5:
            numero += 1
            conta = criar_conta(agencia,numero,cliente)
        if escolha == 6:
            listar(conta)
            
        escolha = menu_opcoes()
main()
