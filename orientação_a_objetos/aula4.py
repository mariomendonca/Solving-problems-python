class Mamifero(object):
  def __init__(self, cor_de_pelo, genero, andar):
    self.cor_de_pelo = cor_de_pelo
    self.genero = genero
    self.num_de_patas = andar

  def falar(self):
    print(f'ola sou um {self.genero} mamifero e sei falar')
  
  def andar(self):
    print(f'estou andando sobre {self.num_de_patas}')

  def amamentar(self):
    if self.genero.lower()[0] == 'm':
      print('Machos nao amamentam')
      return
    print('amamentando meu filhote')

class Pessoa(Mamifero):
  def __init__(self, cor_de_pelo, genero, andar, cabelo):
    super(Pessoa, self).__init__(cor_de_pelo, genero, andar)
    self.cabelo = cabelo

  def falar(self):
    super().falar()
    print('ola sou um maifero sei falar')


# rex = Mamifero('marrom', 'm', 4)
# rex.amamentar()
# rex.andar()
# rex.falar()
julia = Pessoa('preto', 'f', 2, 'loiro')
julia.falar()