entrada = input().split(' ')
op = entrada[0]
num1 = int(entrada[1])
if len(entrada) > 2:
  num2 = int(entrada[2])

if op == 'Soma':
  resultado = num1 + num2
elif op == 'Mult':
  resultado = num1 * num2
elif op == 'Exp': 
  resultado = num1 ** num2
elif op == 'Suc': 
  resultado = num1 + 1

print(resultado)