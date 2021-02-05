n, t = list(map(int, input().split()))
valor_total = 0

for i in range(n):
  c, v = list(map(int, input().split()))
  while (t - c) >= 0:
    valor_total += v
    t -= c
print(valor_total)