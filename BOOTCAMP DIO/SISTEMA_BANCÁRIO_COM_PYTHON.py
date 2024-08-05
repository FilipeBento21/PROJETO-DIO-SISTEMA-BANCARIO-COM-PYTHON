#Começando com o Menu qe será exibido para o usuário:

menu = """

      Olá Bem Vindo !!

Qual Operação Deseja Realizar Hoje ?

[1] Depositar;
[2] Sacar;
[3] Extrato;
[0] Sair;

=> """


#Declarando Variáveis:

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#começando os códigos para as condições do sistema;

while True:

#exibindo menu e interagindo com o usuário;

    opcao = input(menu);

#condições pos trás das opções oferecidas para o usuário no menu

    if opcao == "1":
        deposito = float(input("Informe O Quanto Deseja Depositar = "));
    
        if deposito > 0:
            saldo += deposito;
            extrato += f"Depósito Realizado ! Valor de Depósito: R${deposito:2.2f}\n"
            print(f"""\n                  =============================
                  
                       Deposito Realizado!
                  
                     Saldo Atual: R${saldo:1.2f}

                  =============================""");

        else:
            print("Operação falhou, favor Tentar novamente !");

    elif opcao == "2":
        saque = float(input("Informe O Valor Do Saque: "))

#variáreis definidas com as operações necessárias para as condições da nossa 2º opção do while;
        excedeu_saldo = saque > saldo;

        excedeu_limite = saque > limite;

        excedeu_saques = numero_saques >= LIMITE_SAQUES;

        valor_invalido = saque < 0;
        

        if excedeu_saldo:
            print("Operação falhou, você não possui saldo o suficiente !");

        elif excedeu_limite:
            print("Operação falhou, Valor maior que o valor limite permitido !");

        elif excedeu_saques:
            print("Operação falhou, número de saques máximo Atingido !")

        #Condição principal da opção, porém para executar essa condição se é necessário não se encaixar em nenhuma das alternativas incorretas!!
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque realizado, valor sacado: R${saque:1.2f}\n"
            numero_saques += 1;
            print(f"""\n                  =============================
                  
                      Saque Realizado !!
                  
                    Saldo Atual: R${saldo:1.2f}
                  
                  =============================""");

        else:         
            print("Operação falhou, o valor digitado é Invalido !")

    elif opcao == "3":
        print( "\n===============Vizualizar Extrato ================")
        print("Não foram Realizadas Movimentações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:1.2f}")
        print("==================================================")

    elif opcao == "0":
        break

    else:
        print("""
              Essa opção Não está disponível.
                    Tente Novamente !!
              """)
        

