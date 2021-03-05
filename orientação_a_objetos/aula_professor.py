class No(object):
  def __init__(self, dado=None):
    self.dado = dado
    self._proximo = None
    self._anterior = None
  
  def __str__(self):
    # return f'{self.dado}'
    return str(self.dado)

class Lista(object): 
  def __init__(self):
    self._inicio = None
    self._fim = None

  def isVazia(self):
    if self._inicio == None:
      return True
    return False

  def inserir_no_final(self, dado=None):
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
      if x == i.dado:
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
      s += f' | {i}'
      i = i._proximo
    return s


class Pilha(Lista):
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
        




entrada = [4, 7, 17, 89, 2, 10, 99999]
pilha = Pilha()

for i in entrada:
  pilha.push(i)

pilha.pop()
print(pilha)
  
# if __name__ == '__main__':
# minha_lista = Lista()
# for i in entrada:
#   minha_lista.inserir_no_final(i)

# print(minha_lista)
# no = minha_lista.buscar(3)
# print(no)
# minha_lista.remover(99999)
# print(minha_lista)
