#Começando com o Menu que será exibido para o usuário:

import textwrap;



def menu():

    menu = """\n;
=====================================\n\n
      Olá Bem Vindo !!

Qual Operação Deseja Realizar Hoje ?

[1]\tDepositar;
[2]\tSacar;
[3]\tVer Extrato;
[4]\tNovo Usuário;
[5]\tNova Conta;
[6]\tListar Contas;
[0]\tSair;

=======================================\n\n
=> """
    return input(textwrap.dedent(menu))

def func_deposito(saldo, valor_de_posito, extrato, /):

    if valor_de_posito > 0:
        saldo += valor_de_posito;
        extrato += f"Depósito:\tR$ {valor_de_posito:2.2f}\n"
        print("\n Deposito Realizado com Sucesso !")
    else:
        print("\n@@@ A Operação Falhou, o Valor Informado é Inválido ! @@@\n")

    return saldo, extrato



#começando os códigos para as condições do sistema;

#exibindo menu e interagindo com o usuário;

    opcao = menu();

def func_saque(*, saldo, valor_de_saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_de_saque > saldo
    excedeu_limite = valor_de_saque > limite;
    excedeu_saques = numero_saques >= limite_saques;

    if excedeu_saldo:
        print("\n@@@ Operação Falhou, Sua Conta não Possui Saldo Suficiente Para realizar o Saque ! @@@");

    elif excedeu_limite:
        print("\n@@@ Operação Falhou, o Valor Digitado Ultrapassa o Limite Para realizar o Saque ! @@@");

    elif excedeu_saques:
        print("\n@@@ Operação Falhou, Foi excedido o número de Saque Permitido ! @@@");

    elif valor_de_saque > 0:
        saldo -= valor_de_saque
        extrato += f"Saque:\t\tR$ {valor_de_saque:.2f}\n"
        numero_saques += 1
        print("\n Saque Realizado com Sucesso ! ");
 
    else:
        print("\n@@@ Operação Falhou, O Valor Informado é Invalido ! @@@");

    return saldo, extrato

def func_extrato(saldo, /, *, extrato):

    print( "\n===============Vizualizar Extrato ================");
    print("Não foram Realizadas Movimentações" if not extrato else extrato);
    print(f"\n Saldo: R${saldo:1.2f}");
    print("==================================================")

def novo_usuario(usuarios):
    cpf = float(input("Informe o seu CPF (APENAS NÚMEROS): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário cadastrado com esse CPF !")
        return

    else:

        nome_usuario = input("\n\nInforme o seu nome completo: ");
        data_nasciimento_usuario = input("\n Informe sua data de nascimento (dd/mm/aaaa): ");
        endereco_usario = input("\n Informe seu Endereço(longadouro, nro, bairro, cidade(sigla estado)): ");

        usuarios.append({"nome": nome_usuario, "Data de Nascimento": data_nasciimento_usuario, "endereço": endereco_usario})

        print("\n\nNovo usuário criado com Sucesso !");

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios, /):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:

        print("\n Conta criada com sucesso !");
        return {"agencia": agencia, "número_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontado, Encerrando Processo de Criação;")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C\t\t{conta["numero_conta"]}
            TItular:\t{conta["usuario"]['nome']}
        """

    print("=" * 100);
    print(textwrap.dedent(linha))


def main():

#Declarando Variáveis Imutáveis:
    LIMITE_SAQUES = 3;
    AGENCIA = "0001";

#Declarando Variáveis Mutáveis:
    saldo = 0;
    limite = 500;
    extrato = "";
    numero_saques = 0;
    usuarios = [];
    contas = [];
    
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "));
        
            saldo, extrato = func_deposito(saldo, valor, extrato);

        elif opcao == "2":
            valor_de_saque = float(input("Informe o Valor do Saque: "));
    
            saldo, extrato = func_saque(
                saldo=saldo,
                valor_de_saque=valor_de_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            );
        
        elif opcao == "3":
            extrato = func_extrato(saldo, extrato=extrato);

        elif opcao == "4":
            novo_usuario(usuarios);
        
        elif opcao == "5":
            numero_conta = len(contas) + 1;
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas);

        


    else:
        print("Operação Falhou, Favor tentar novamente !");


main()