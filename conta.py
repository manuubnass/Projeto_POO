class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    #Para que o saldo fique protegido, ele é encapsulado com o metodo get
    #def get_saldo(self):
    #    return self._saldo
    #Ou inves do get, dá para usar o property, declarando uma função que obtenha o valor do saldo
    @property
    def saldo(self):
        return self._saldo

    #Caso o saldo seja negativo ele retorna o erro, se não ele associa o saldo ao saldo encapsulado
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    # self.saldo -= valor lê o saldo atual usando o getter,
    # subtrai o valor do saque e tenta salvar o novo saldo.
    # Ao salvar, o setter é chamado, garantindo que o saldo
    # não fique negativo e mantendo o encapsulamento.
    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo -= valor
            print("Saque de ", valor, " realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor
        print("Deposito de ", valor ," realizado com sucesso")

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo Atual: ", self.saldo)
