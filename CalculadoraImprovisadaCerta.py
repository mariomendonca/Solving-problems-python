def Sucessor(a):
  return a + 1

def Soma(a, b):
  resultado = a
  for i in range(b):
    resultado = Sucessor(resultado)
  return resultado

def Mult(a, b):
  resultado = 0
  for i in range(b):
    resultado = Soma(resultado, a)
  return resultado

def Exp(a, b):
  resultado = 1
  for i in range(b):
    resultado = Mult(resultado, a)
  return resultado

entrada = input().split(' ')
op = entrada[0]
num1 = int(entrada[1])
if len(entrada) > 2:
  num2 = int(entrada[2])

if op == 'Suc':
  print(Sucessor(num1))

elif op == 'Soma':
  print(Soma(num1, num2))

elif op == 'Mult':
  print(Mult(num1, num2))

elif op == 'Exp': 
  print(Exp(num1, num2))