n, t = list(map(int, input().split()))
valor_total = 0

for i in range(n):
  c, v = list(map(int, input().split()))
  if (t - c) >= 0:
    valor_total += v
    t -= c
print(valor_total)

"""
primeira linha
n = numero de tamanhos de canos
t = tamanho 

n linhas
c = comprimento
v = valor
"""
