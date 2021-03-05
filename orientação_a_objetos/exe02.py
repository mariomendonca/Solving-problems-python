class Banco(object):
  def __init__(self, total, taxa_reserva, reserva_exigida):
    self.__total = total
    self.taxa_reserva = taxa_reserva
    self.__reserva_exigida = reserva_exigida

  def __calcular_reserva(self):
    reserva = self.__total * self.taxa_reserva
    return reserva

  def podeFazerEmprestimo(self, valor):
    if valor + self.__reserva_exigida <= self.__total:
      return True
    else: 
      return False

nu = Banco(1000, 0.05, 50)
print(nu.podeFazerEmprestimo(400))