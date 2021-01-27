def maior_digito(A, i, j):
  maior_indice = k = i
  while k <= j:
    if A[k] > A[maior_indice]:
      maior_indice = k
    k += 1
  return maior_indice

while True:
  parametros = [int(i) for i in input().split()]
  if parametros: 
    num_digitos_entrada, num_digitos_removidos = parametros
    digitos_entrada = [int(i) for i in input()]
    num_digitos_restantes = num_digitos_entrada - num_digitos_removidos
    posicao_do_maior = -1
    for i in range(num_digitos_restantes):
      posicao_do_maior = maior_digito(digitos_entrada, posicao_do_maior + 1, (num_digitos_entrada - 1) - (num_digitos_restantes - 1 - i))
      print(digitos_entrada[posicao_do_maior], end='')
    print()
  else:
    break


"""
pesquisar o maior numero em um determinado trecho de um array 
prxima janela comeca do return + 1 (o indice)
1 loop
print(digito, end="")
"""