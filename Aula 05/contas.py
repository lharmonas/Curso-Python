class Conta:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar (self,valor):
        self.saldo += valor
        self.mostra_saldo()

    def sacar (self,valor):
        if self.saldo < valor:
            print(f'Não foi possível realizar o saque.\nSacar no máximo *R${self.saldo}*')
        else:
            self.saldo -= valor
            self.mostra_saldo()

    def mostra_saldo (self):
        print(f'Olá {self.titular}!\nSeu saldo é de: R${self.saldo}')