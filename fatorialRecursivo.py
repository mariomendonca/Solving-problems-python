def fatorial(n):
  print(f'calculando fatorial de {n}')
  if n <= 1: 
    return 1
  else: 
    return n * fatorial(n - 1)


print(fatorial(1))
print(fatorial(7))