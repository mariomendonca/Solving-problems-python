class Objeto_Grafico(object):
  def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno):
    self.cor_de_preenchimento = cor_de_preenchimento
    self.preenchida = preenchida
    self.cor_de_contorno = cor_de_contorno

class Retangulo(Objeto_Grafico):
  def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
    super().__init__(cor_de_contorno, preenchida, cor_de_preenchimento)
    self.base = base
    self.altura = altura

  def perimetro(self):
    p = (2 * self.altura) + (2 * self.base)
    return p

  def area(self):
    a = self.base * self.altura
    return a

ret = Retangulo(2, False, 1, 25, 10)

# print(ret.cor_de_contorno, ret.cor_de_preenchimento, ret.preenchida)
print('area', ret.area(), 'perimetro',  ret.perimetro())