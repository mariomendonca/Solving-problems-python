entrada = input().split()
total = 0
lista = []
for x in entrada:
    if x == 'INICIO':
        lista.append(x)
    elif x == 'LOOP':
        lista.append(entrada[entrada.index(x)+1])
        entrada.pop(entrada.index(x))
        lista.append('*')
    elif x == 'OP':
        lista.append(entrada[entrada.index(x)+1])
        entrada.pop(entrada.index(x))
    elif x == 'FIM':
        while lista[-1] != 'INICIO'and lista[-1] !='*':
            total += int(lista.pop())
        if lista[-1]=='*':
            lista.pop()
            total*=int(lista.pop())
print(total)