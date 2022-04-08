import math
T = int(input())
for i in range (T):
  X, Y = input().split()
  X = int(X) 
  Y = int(Y) 
  K = 2 # X<Y 
  if (X>Y):
    K = math.ceil(X/Y)
  print(K) 