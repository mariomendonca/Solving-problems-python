class Meu_Objeto(object):
  def __init__(self, nome, idade = 0):
    self.nome = nome
    self.idade = idade
    print('Construtor chamado com suceso')

  def imprime(self, x):
    print(f'Ola meu nome é {self.nome} e eu tenho {self.idade}')
    print(x)

# Meu_Objeto().imprime()
x = Meu_Objeto('mario', 20)
x.imprime(5)