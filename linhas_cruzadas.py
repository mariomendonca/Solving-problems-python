n = int(input())
entrada = list(map(int, input().split()))
cruzamentos = 0

for i in range (n):
  for j in range(i + 1,  n):
    if entrada[i] > entrada[j]:
      cruzamentos += 1

print(cruzamentos)
