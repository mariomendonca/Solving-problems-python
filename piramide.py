def piramide(n):
    blocos = 0
    for i in range(n + 1):
        blocos += i
    print(blocos)

piramide(5)