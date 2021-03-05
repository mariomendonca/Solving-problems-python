# class Minha:
#   def __init__(self):
#     self.x = 0
#     self.y = 0

class Pessoa:
  def __init__(self, nome, peso, cao):
    self.nome = nome
    self.peso = peso
    self.cao = cao

  def treinar(self):
    self.cao.da_a_patinha()
    self.cao.latir()



class Cachorro():
  def __init__(self, nome, cor):
    self.nome = nome
    self.cor = cor
  def da_a_patinha(self):
    print(f'{self.nome} extendeu a patinha')

  def latir(self):
    print('AUAUAUAUAU')
  

rex = Cachorro('Rex', 'marrom')
joao = Pessoa('joao', 60, rex)

joao.treinar()