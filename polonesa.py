class No:
  def __init__(self, dado):
    self._dado = dado
    self._prox_dado = None

  def get_dado(self):
    return self._dado

  def get_prox_no(self):
    return self._prox_dado

  def set_prox_no(self, novoDado):
    self._prox_dado = novoDado


class Lista:
  def __init__(self):
    self._primeiro_no = None
    self._ultimo_no = None

  def isVazio(self):
    return self._primeiro_no == None

  def Inserir_no_inicio(self, dado):
    novo_No = No(dado)
    if self.isVazio():
      self._primeiro_no = self._ultimo_no = novo_No
    else:
      novo_No.set_prox_no(self._primeiro_no)
      self._primeiro_no = novo_No

  def Remover_do_inicio(self):
    primeiro_no = self._primeiro_no.get_dado()
    if self._primeiro_no == self._ultimo_no:
      self._primeiro_no = self._ultimo_no = None
    else:
      self._primeiro_no = self._primeiro_no.get_prox_no()
    return primeiro_no

  def __str__(self):
    if self.isVazio():
      return 'Lista vazia'
    No = self._primeiro_no
    string = ""
    while No != None:
      string += str(No.get_dado())+ " "
      No = No.get_prox_no()
    return string

class Pilha(Lista):
  def empilhar(self, dado):
    self.Inserir_no_inicio(dado)

  def desempilhar(self):
    return self.Remover_do_inicio()


while True:  
  operadores = ['*', '/', '-', '+']
  entrada = input().split(' ')
  if entrada[0] != '':
    entrada = entrada[::-1]
    pilha = Pilha()
    for i in range(len(entrada)):
      if entrada[i] not in operadores:
        pilha.empilhar(int(entrada[i]))
      else:
        x = pilha.desempilhar()
        y = pilha.desempilhar()
        if entrada[i] == '+':
          pilha.empilhar(int(x + y))
        elif entrada[i] == '-':
          pilha.empilhar(int(x - y))
        elif entrada[i] == '*':
          pilha.empilhar(int(x * y))
        elif entrada[i] == '/':
          pilha.empilhar(int(x / y))
    print(pilha)
  else:
    break
