class No(object):
  def __init__(self, dado=None):
    self._dado = dado
    self._proximo = None
    self._anterior = None

  def __str__(self):
    return f'{self._dado}'

class Lista(object):
  def __init__(self):
    self._inicio = None
    self._fim = None

  def isVazia(self):
    if self._inicio == None:
      return True

  def inserir_no_fim(self, dado=None):
    novo_no = No(dado)
    if self.isVazia():
      self._inicio = self._fim = novo_no
    else: 
      novo_no._anterior = self._fim
      self._fim._proximo = novo_no
      self._fim = novo_no

  def buscar(self, x):
    i = self._inicio
    while i != None:
      if x == i._dado:
        break
      else: 
        i = i._proximo
    return i

  def remover(self, x):
    no_encontrado = self.buscar(x)
    if no_encontrado != None:
      if no_encontrado._anterior != None:
        no_encontrado._anterior._proximo = no_encontrado._proximo
      else:
        self._inicio = no_encontrado._proximo
      if no_encontrado._proximo != None:
        no_encontrado._proximo._anterior = no_encontrado._anterior
      else: 
        self._fim = no_encontrado._anterior
    return no_encontrado

  def __str__(self):
    s = ''
    i = self._inicio
    while i != None:
      s += f'{str(i)} '
      i = i._proximo
    return s

lista = Lista()
n = int(input())
entrada = list(map(int, input().split()))
for i in range(n):
  lista.inserir_no_fim(entrada[i])
  i += 1

m = int(input())
desistencias = list(map(int, input().split()))
for i in range(m):
  lista.remover(desistencias[i])
  i += 1


print(lista)




