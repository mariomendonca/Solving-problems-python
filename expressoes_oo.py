class No(object):
  def __init__(self, dado=None):
    self.dado = dado
    self._proximo = None
    self._anterior = None

  def __str__(self):
    return str(self.dado)

class Pilha(object):
  def __init__(self):
    self._inicio = None
    self._fim = None

  def isVazia(self):
    if self._inicio == None:
      return True
    return False

  def buscar_primeiro(self):
    i = self._inicio
    return i

  def buscar(self, x):
    i = self._inicio
    while i != None:
      if x == i._dado:
        break
      else: 
        i = i._proximo
    return i

  def push(self, dado=None):
    novo_no = No(dado)
    if self.isVazia():
      self._fim = novo_no
    else:
      novo_no._proximo = self._inicio
      self._inicio._anterior = novo_no
    self._inicio = novo_no

  def pop(self):
    no = self._inicio 
    if not self.isVazia():
      if no._proximo == None:
        self._fim = None
      else: 
        no._proximo._anterior = None
      self._inicio = no._proximo

  def __str__(self):
    s = ''
    i = self._inicio
    while i != None:
      s += f'{i}'
      i = i._proximo
    return s


n = int(input())

for i in range(n):
  string = input()
  pilha = Pilha()
  for x in string:
    if x == '(' or x == '{' or x == '[':
      pilha.push(x)
    elif x == ')':
      if pilha.isVazia():
        pilha.push(x)
      elif str(pilha.buscar_primeiro()) == '(':
        pilha.pop()

    elif x == '}':
      if pilha.isVazia():
        pilha.push(x)
      elif str(pilha.buscar_primeiro()) == '{':
        pilha.pop()    

    elif x == ']':
      if pilha.isVazia():
        pilha.push(x)
      elif str(pilha.buscar_primeiro()) == '[':
        pilha.pop()

  if pilha.isVazia():
    print('S')
  else: 
    print('N')
        