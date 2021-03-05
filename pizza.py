def somando(parte):
  somatorio = 0
  for i in parte:
    somatorio += i
  
  return somatorio

n = int(input())
maior_valor = 0

fatias = [int(x) for x in input().split(' ')]
fatias = fatias * 2

for i in range(len(fatias)):
  for j in range(i, n + 1 + i):
    soma = somando(fatias[i:j])
    if maior_valor < soma:
      maior_valor = soma

print(maior_valor)
