class tabela_hash:
    def __init__(self, n):
        self._lenght = n
        self._items = [None] * n
        self._values = [None] * n

    def hash_function(self, key):
        h = int(key, 2) % self._lenght
        return h

    def insert_in_table(self, key):
        i = self.hash_function(key)
        self._items[i] = key
        self._values[i] = 1
        return None

    def search(self, key):
        i = self.hash_function(key)
        if self._items[i] is None:
            return False
        else:
            return self._items[i]

    def add_in_value(self, val, key):
        i = self.hash_function(key)
        if self.search(key) is not False:
            self._values[i] += val
        return self._values[i]

    def get_value(self, key):
        i = self.hash_function(key)
        if self.search(key) is not False:
            return self._values[i]

def greater(a, b):
    return (a + b + module(a - b)) // 2

def module(a):
    if a > 0:
        return a
    else:
        return -a


maior = 0
m, n = [int(x) for x in input().split()]
planos = [[None for i in range(4)] for j in range(m)]
regioes = tabela_hash(20001)

for i in range(m):
    planos[i][0], planos[i][1], planos[i][2], planos[i][3] = [int(x) for x in input().split()]

for i in range(n):
    key = ''
    X, Y, Z = [int(x) for x in input().split()]
    for j in range(m):
        if planos[j][0] * X + planos[j][1] * Y + planos[j][2] * Z > planos[j][3]:
            key += '0'
        else:
            key += '1'
    if key == regioes.search(key):
        regioes.add_in_value(1, key)
    else:
        regioes.insert_in_table(key)

    maior = greater(regioes.get_value(key), maior)

print(maior)
