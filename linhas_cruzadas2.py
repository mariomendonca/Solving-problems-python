n = int(input())
entrada = list(map(int, input().split()))
cruzamentos = 0
i = 0
while i < n - 1:
  for j in range(i + 1,  n):
    if entrada[i] > entrada[j]:
      cruzamentos += 1
  i += 1

print(cruzamentos)