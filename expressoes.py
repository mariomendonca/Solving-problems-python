n = int(input())

for i in range(n):
  string = input()
  lista = []
  for x in string:
    if x == '(' or x == '{' or x == '[':
        lista.append(x)
    elif x == ')' :
        if len(lista) == 0: 
            lista.append(x)
            
        elif len(lista) > 0 and lista[-1] == '(' :
            lista.pop()

    elif x == '}':
        if len(lista) == 0  : 
            lista.append(x)
            
        elif len(lista) > 0 and lista[-1] == '{' :
            lista.pop()
    elif x == ']':
        if len(lista) == 0  : 
            lista.append(x)
            
        elif len(lista) > 0 and lista[-1] == '[' :
            lista.pop()
    
  if len(lista) == 0:
    print('S')
  else:
    print('N')
