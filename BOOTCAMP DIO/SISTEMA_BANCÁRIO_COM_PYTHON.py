#Começando com o Menu que será exibido para o usuário:

import textwrap;

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

    else:
        print("Operação Falhou, Favor tentar novamente !");


def menu():

    menu = """\n;
=====================================\n\n
      Olá Bem Vindo !!

Qual Operação Deseja Realizar Hoje ?

[1]\tDepositar;
[2]\tSacar;
[3]\tVer Extrato;
[4]\tNova Conta;
[5]\tListar contas;
[6]\tNovo usuário;
[0]\tSair;

=======================================\n\n
=> """
    return input(textwrap.dedent(menu));

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

def func_extrato(saldo, /, *, extrato):

    print( "\n===============Vizualizar Extrato ================");
    print("Não foram Realizadas Movimentações" if not extrato else extrato);
    print(f"\n Saldo: R${saldo:1.2f}");
    print("==================================================")


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


main()



#        excedeu_saldo = saque > saldo;
#
#        excedeu_limite = saque > limite;
#
#        excedeu_saques = numero_saques >= LIMITE_SAQUES;
#
#        valor_invalido = saque < 0;
        

#        if excedeu_saldo:
#            print("Operação falhou, você não possui saldo o suficiente !");

#        elif excedeu_limite:
#            print("Operação falhou, Valor maior que o valor limite permitido !");

#        elif excedeu_saques:
#            print("Operação falhou, número de saques máximo Atingido !")

        #Condição principal da opção, porém para executar essa condição se é necessário não se encaixar em nenhuma das alternativas incorretas!!
#        elif saque > 0:
#            saldo -= saque
#            extrato += f"Saque realizado, valor sacado: R${saque:1.2f}\n"
#            numero_saques += 1;
#            print(f"""\n                  =============================
#                 
#                     Saque Realizado !!
                  
#                    Saldo Atual: R${saldo:1.2f}
                  
#                  =============================""");

#        else:         
#            print("Operação falhou, o valor digitado é Invalido !")

#    elif opcao == "3":
#        print( "\n===============Vizualizar Extrato ================")
#        print("Não foram Realizadas Movimentações" if not extrato else extrato)
#        print(f"\n Saldo: R${saldo:1.2f}")
#        print("==================================================")

#    elif opcao == "0":
        
        

#        print("""
#              Essa opção Não está disponível.
#                    Tente Novamente !!
#              """)