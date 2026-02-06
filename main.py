from cliente import Cliente #Importação da classe Cliente
from conta import Conta
class Main:
    pass

c1 = Cliente("João", "119999-9999") #Objeto do cliente

conta_c1 = Conta(c1._nome, 6564, 0) #Objeto da conta

conta_c1.deposito(100) #Depositando 100 reais
conta_c1.saque(50)
conta_c1.extrato()
