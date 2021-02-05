class Animal: #super
  def __init__(self, nome=None, com_fome=False):
    self._nome = nome # nome = atributo protegido (protected)
    self.com_fome = com_fome # publico

  def comer(self):
    print(f'O animal {self._nome} está comendo')

  def locomover(self): #metodo abstrato = sera implementado na subclass
    pass 

class Ave(Animal):
  def __init__(self, nome=None, com_fome=False, cor_penas='branca'):
    super().__init__(nome, com_fome) #chamando o contrutor de animal
    self.cor_penas = cor_penas

  def locomover(self):
    print(f'A Ave {self._nome} pode se locomover andando')

class Pinguim(Ave):
  def escorregar(self):
    print(f'O pinguim {self._nome} está escorregando')

  def comer(self):
    super().comer()
    print(f'O pinguim {self._nome} come pescando')

class Andorinha(Ave):
  def locomover(self):
    print(f'a andorinha {self._nome} se locomove voando com suas asas')

class Mamifero(Animal):
  def mamar(self):
    print(f'o mamifero {self._nome} esta mamando')

class Cavalo(Mamifero):
  def locomover(self):
    print(f'o cavalo {self._nome} se locomove com 4 patas')

  def comer(self):
    self.mamar()
    print(f'o cavalo {self._nome} come grama, pasto')

class Humano(Animal):
  def locomover(self):
    print(f'O humano {self._nome} se locomove com 2 pes')


pinguim = Pinguim('happy feet', True, 'cinza')
andorinha = Andorinha('azeite', False, 'preta') 
cavalo = Cavalo('pe de pano', True)
humano = Humano('pedro', True)

lista = [pinguim, andorinha, humano, cavalo]
# for i in lista:
#   i.locomover()

for Animal in lista:
  Animal.comer()