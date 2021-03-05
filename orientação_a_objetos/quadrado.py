class Quadrado():
  def __init__(self, lado):
    self.lado = lado

  def valor_do_lado(self):
    return self.lado

  def calcular_area(self):
    return self.lado * self.lado

  def mudar_lado(self, x):
    self.lado = x
    return self.lado

x = Quadrado(5)
print(x.valor_do_lado())
print(x.calcular_area())
print(x.mudar_lado(7))
print(x.calcular_area())