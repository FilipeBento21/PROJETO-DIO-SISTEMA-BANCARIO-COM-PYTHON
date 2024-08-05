#Começando com o Menu qye será exibido para o usuário:

menu = """

Qual Operação Deseja Realizar ?

[1] Depositar;
[2] Sacar;
[3] Extrato;
[0] Sair;

=> """
#exibindo menu e interagindo com o usuário;

#Declarando Variáveis:

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu);

    if opcao == "1":
        deposito = float(input("Informe O Quanto Deseja Depositar = "));
    
        if deposito > 0:
            saldo += deposito;
            extrato += f"Depósito Realizado ! Valor de Depósito: R${deposito:2.2f}\n"

        else:
            print("Operação falhou, favor Tentar novamente !");

    elif opcao == "2":
        saque = float(input("Informe O Valor Do Saque: "))

        excedeu_saldo = saque > saldo;

        if excedeu_saldo:
            print("Operação falhou, você não possui saldo o suficiente !")

        excedeu_limite = saque > limite
        
        if excedeu_limite:
            print("Operação falhou, Valor maior que o valor limite permitido !")

        excedeu_saques = numero_saques >= LIMITE_SAQUES;

        if excedeu_saques:
            print("Operação falhou, número de saques máximo Atingido !")
         
        if saque > 0:
            saldo -= saque
            extrato += f"Saque realizado, valor sacado: R${saque:1.2f}\n"
            numero_saques += 1;
        
        valor_invalido = saque < 0

        if valor_invalido:
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
        

