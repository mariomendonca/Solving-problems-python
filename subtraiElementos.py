def subtraiElementos(listaNums):
    contador = 0
    for item in listaNums:
        contador += item

    contador -= listaNums[0] 
    resultado = listaNums[0] - contador
    print(resultado)

    
subtraiElementos([100,20,4,10])
subtraiElementos([3, 10, 5])






# 1. Defina uma função com o nome “subtraiElementos”, 
# que receba como parâmetros uma lista de números inteiros (listaNums) 
# e cujo corpo apresente um código NÃO recursivo que subtraia todos os 
# elementos dessa lista e apresente o resultado na tela. Para testar passe 
# uma lista com os valores [100, 20, 4, 10], a saída esperada é 66. (Copie aqui seu código) (1,0):
# 10 pontos