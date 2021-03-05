class No():
  def __init__(self, dado=None):
    self._dado = dado
    self._proximo = None
    self._ant = None

  def __str__(self):
    return f'Dado: {self._dado}'

class Lista():
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
      novo_no._ant = self._fim
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

  def removerElemento(self, x):
    no_encontrado = self.buscar(x)
    if no_encontrado != None:
      if no_encontrado._ant != None:
        no_encontrado._ant._proximo = no_encontrado._proximo
      else:
        self._inicio = no_encontrado._proximo
      if no_encontrado._proximo != None:
        no_encontrado._proximo._ant = no_encontrado._ant
      else: 
        self._fim = no_encontrado._ant
    return no_encontrado
  
  def remover_do_inicio(self):
    no = self._inicio
    if not self.isVazia():
      # if self._inicio = self._fim: #apenas 1 elemento
        if no._proximo == None:
          self._fim = None
        else: 
          no._proximo._ant = None
        self._inicio = no._proximo
    return no

  def __str__(self):
    s = ''
    i = self._inicio
    while i != None:
      s += f' | {str(i)}'
      i = i._proximo
    return s
  

class Fila(Lista):
  def inserir(self, dado):
    self.inserir_no_fim(dado)
  def remover(self, dado):
    self.remover_do_inicio()


class Pilha(Lista):
  def push(self, dado=None):
    novo_no = No(dado)
    if self.isVazia():
      self.fim = novo_no
    else: 
      novo_no._proximo = self._inicio
      self._inicio._ant = novo_no
    self._inicio = novo_no

  def pop(self):
    return self.remover_do_inicio()

if __name__ == '__main__':
  entrada = [4, 7, 17, 89, 2, 10]
  lista = Lista()
  fila = Fila()
  pilha = Pilha()
  for i in entrada:
    # lista.inserir_no_fim(i)
    # fila.inserir(i)
    # fila.remover_do_inicio(4)
    pilha.push(i)
    pilha.pop()

  # print(fila)
  print(pilha)


  # lista.remover(4)
  # lista.inserir_no_fim(99)