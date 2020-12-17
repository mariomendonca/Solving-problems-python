n = int(input())
lista = list(map(int, input().split()))
contador = 1
somaTotal = 0
somaAtual = 0

for i in range(n):
  somaTotal += contador
  contador = contador + 1

for x in lista:
  somaAtual += x

print(somaTotal - somaAtual)
