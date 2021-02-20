lista_de_tamanhos = [[0,0] for i in range(31)]
pares = 0

n = int(input())

for i in range(n):
  bota = input().split()
  index = (int(bota[0]) - 30)
  if bota[1] == 'E':
    if lista_de_tamanhos[index][1] > 0:
      pares += 1
      lista_de_tamanhos[index][1] -= 1
    else:
      lista_de_tamanhos[index][0] += 1
  
  if bota[1] == 'D':
    if lista_de_tamanhos[index][0] > 0:
      pares += 1
      lista_de_tamanhos[index][0] -= 1
    else:
      lista_de_tamanhos[index][1] += 1

print(pares)
# print(lista_de_tamanhos) 
