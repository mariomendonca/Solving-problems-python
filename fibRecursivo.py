def fib(n):
  print(f'calculando fib de {n}')
  if n <= 1:
    return n
  else: 
    return fib(n - 2) + fib(n - 1)

print(fib(7))
# fib(10)
# print(fib(100))