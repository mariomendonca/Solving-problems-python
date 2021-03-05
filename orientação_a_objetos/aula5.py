# class ObejetoGrafico(object):
#   def __init__(self, cor):
#     self.cor = cor
# # metodos abstratos, esperar q as subclasses dessa classe preencham isso
#   def area(self):
#     pass
#   def perimetro(self):
#     pass
#   def info(self):
#     print(f'{self.area} metros2 serao preenchidos com a cor {self.cor}')


class Conta(object):
  total = 10000
  reserva = 0.1
  def __init__(self, ID, saldo):
    self.ID = ID
    self.saldo = saldo

  def deposito(self, valor):
    self.saldo += valor
    return self.saldo
  
  def saque(self, valor):
    if self.saldo > valor:
      self.saldo -= valor
      return self.saldo

nubank = Conta(123, 10000)
print(nubank.deposito(500), nubank.saque(100), nubank.saldo)