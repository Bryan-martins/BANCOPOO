class Conta:
    def __init__(self, numero, cliente, saldo, limite = 10000):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def deposita(self, valor):
        if self.saldo <= 10000 and valor <= 10000 - self.saldo :
            self.saldo += valor
            self.historico.mov.append('Deposito de R$ {}'.format(valor))
            return True

        else:
            print('Sem limite!')
            return False

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.mov.append('Saque de R$ {}'.format(valor)) 
            return True
        else:
            print('Sem saldo! ')
            return False
    
    def extrato(self):
        print('Saldo: {} \nConta: {}'.format(self.saldo, self.numero))
        self.historico.mov.append('Tirado o extrato!, saldo de R$ {}'.format(self.saldo))
    
    def transfere(self, contas, valor):
        opc = int(input('Digite a conta para qual vai transferir: '))

        for x in contas:
            if x.numero == opc:     
                res = self.saca(valor)
                if res:
                    res2 = x.deposita(valor)
                    if res2:
                        self.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(x.numero,valor))
                    
                    else:
                        print('la')
                        print('Erro! ')
                        self.deposita(valor)
                else:
                    return False

    def menu(self, contas):
        cont = 1

        while cont != 0:
            print('MENU: ')
            print('1 - Depositar: ')
            print('2 - Sacar: ')
            print('3 - Extrato: ')
            print('4 - Transferir: ')
            print('5 - Historico: ')
            print('0 - Sair: ')
            opc = int(input())

            if opc == 1:
                valor = float(input('Digite o valor: '))
                self.deposita(valor)
                print()
            
            elif opc == 2:
                valor = float(input('Digite o valor: '))
                self.saca(valor)
                print()

            elif opc == 3:
                self.extrato()
                print()
            
            elif opc == 4:
                valor = float(input('Digite o valor: '))
                self.transfere(contas, valor)
                print()
            
            elif opc == 5:
                print('Abertura da conta:', self.historico.abertura)
                for x in range(len(self.historico.mov)):
                    print('-', self.historico.mov[x])
                
                print()
        
            elif opc == 0:
                cont = 0

            else:
                print('Digite uma opção válida! ')
                print()


class Cliente:
    def __init__(self, nome, sn, cpf):
        self.nome = nome
        self.sn = sn
        self.cpf = cpf

import datetime

class Historico:
    def __init__(self):
        self.abertura = datetime.datetime.today()
        self.mov = []
