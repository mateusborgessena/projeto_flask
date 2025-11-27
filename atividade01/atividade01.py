class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print("Erro: Não é possível depositar valores negativos!")
            return False
        
        self.saldo += valor
        return True

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        
        print("Erro: Saldo insuficiente para sacar!")
        return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de {valor} realizada com sucesso!")
            return True
        
        print("Transferência não realizada.")
        return False



conta_a = Conta("João", 500)
conta_b = Conta("Maria", 300)

conta_a.transferir(200, conta_b)

print("Saldo da conta_a:", conta_a.saldo) 
print("Saldo da conta_b:", conta_b.saldo)  

conta_b.depositar(-50)  