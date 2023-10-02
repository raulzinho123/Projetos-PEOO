class ContaBancaria:
    def _init_(self, numero, titular, saldo=0.0):
        #Faz as contas com número, titular e saldo (com valor padrão de 0.0)
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        #Serve pra adicionar o valor ao saldo da conta
        self.saldo += valor
        return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"

    def sacar(self, valor):
        #Serve para verificar se tem saldo suficiente antes de sacar
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente."

    def transferir(self, destino, valor):
        #Transfere um valor para outra conta, verificando saldo suficiente
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            return f"Transferência de {valor} realizada para a conta {destino.numero}. Seu novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente para transferência."

    def exibir_saldo(self):
        #Retorna uma mensagem com o saldo atual da conta
        return f"Saldo atual da conta {self.numero} (Titular: {self.titular}): {self.saldo}"


conta1 = ContaBancaria(1, "Raul")
conta2 = ContaBancaria(2, "Elysson", 500.0)

print(conta1.depositar(1000.0))
print(conta1.sacar(200.0))
print(conta1.exibir_saldo())

print(conta2.transferir(conta1, 300.0))
print(conta1.exibir_saldo())
print(conta2.exibir_saldo())