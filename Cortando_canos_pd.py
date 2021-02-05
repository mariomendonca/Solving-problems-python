n, t = list(map(int, input().split()))
tamanhos = []
valores = []

for i in range(n):
  c, v = list(map(int, input().split()))
  valores.append(v)
  tamanhos.append(c)

def maior(a, b):
  if a > b:
    return a 
  else:
    return b

def cortando_canos(n, t):
  matriz = [None] * (n + 1) 
  for i in range(n + 1):
    comprimentos = [None] * (t + 1) 
    matriz[i] = comprimentos

  for i in range(n + 1): 
    for j in range(t + 1): 
      if i == 0 or j == 0: 
        matriz[i][j] = 0
      elif tamanhos[i-1] <= j: 
        matriz[i][j] = maior(valores[i-1] + matriz[i-1][j-tamanhos[i-1]],  matriz[i-1][j]) 
      else: 
        matriz[i][j] = matriz[i-1][j] 

  return matriz[n][t]

print(cortando_canos(n, t))
