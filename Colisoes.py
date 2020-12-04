Xa0, Ya0, Xa1, Ya1 = list(map(int, input().split()))
Xb0, Yb0, Xb1, Yb1 = list(map(int, input().split()))

if ((Xa1 < Xb0) or (Xa0 > Xb1)) and ((Ya1 < Yb0) or (Ya0 > Yb1)):
  print(0)
else:
  print(1)
