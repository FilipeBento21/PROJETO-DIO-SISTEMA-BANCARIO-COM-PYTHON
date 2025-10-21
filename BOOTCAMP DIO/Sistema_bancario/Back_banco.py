# Back_banco.py

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class ContaBancaria:
    LIMITE_SAQUE = 500
    LIMITE_SAQUES_DIA = 3
    AGENCIA = "0001"
    
    def __init__(self, numero_conta, usuario):
        self.numero_conta = numero_conta
        self.agencia = self.AGENCIA
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
    
    def depositar(self, valor):
        """Realiza um depósito na conta"""
        if valor <= 0:
            return False, "❌ Valor inválido para depósito!"
        
        self.saldo += valor
        self.extrato.append({
            'tipo': 'Depósito',
            'valor': valor,
            'data': self._obter_data_hora()
        })
        return True, f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!"
    
    def sacar(self, valor):
        """Realiza um saque da conta"""
        if valor <= 0:
            return False, "❌ Valor inválido para saque!"
        
        if valor > self.saldo:
            return False, "❌ Saldo insuficiente!"
        
        if valor > self.LIMITE_SAQUE:
            return False, f"❌ Valor excede o limite de R$ {self.LIMITE_SAQUE:.2f} por saque!"
        
        saques_hoje = self._contar_saques_hoje()
        if saques_hoje >= self.LIMITE_SAQUES_DIA:
            return False, f"❌ Limite de {self.LIMITE_SAQUES_DIA} saques diários atingido!"
        
        self.saldo -= valor
        self.extrato.append({
            'tipo': 'Saque',
            'valor': valor,
            'data': self._obter_data_hora()
        })
        return True, f"✅ Saque de R$ {valor:.2f} realizado com sucesso!"
    
    def consultar_saldo(self):
        """Retorna o saldo atual"""
        return self.saldo
    
    def ver_extrato(self):
        """Retorna o extrato completo"""
        return self.extrato
    
    def _contar_saques_hoje(self):
        """Conta quantos saques foram feitos hoje"""
        from datetime import datetime
        hoje = datetime.now().strftime("%d/%m/%Y")
        return sum(1 for e in self.extrato 
                  if e['tipo'] == 'Saque' and e['data'].startswith(hoje))
    
    def _obter_data_hora(self):
        """Retorna data e hora atual formatada"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []
    
    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        """Cria um novo usuário"""
        if self.filtrar_usuario(cpf):
            return False, "❌ CPF já cadastrado!"
        
        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        return True, f"✅ Usuário {nome} criado com sucesso!"
    
    def filtrar_usuario(self, cpf):
        """Busca um usuário pelo CPF"""
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
    
    def criar_conta(self, cpf):
        """Cria uma nova conta bancária"""
        usuario = self.filtrar_usuario(cpf)
        
        if not usuario:
            return False, "❌ Usuário não encontrado! Cadastre-se primeiro."
        
        numero_conta = len(self.contas) + 1
        nova_conta = ContaBancaria(numero_conta, usuario)
        self.contas.append(nova_conta)
        
        return True, f"✅ Conta {numero_conta} criada com sucesso!"
    
    def listar_contas(self):
        """Retorna todas as contas cadastradas"""
        return self.contas
    
    def listar_usuarios(self):
        """Retorna todos os usuários cadastrados"""
        return self.usuarios