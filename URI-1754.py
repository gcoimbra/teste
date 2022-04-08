#URI - 1754 - A Sala do Tempo
import math
T = int(input())
for i in range (T):
  X, Y = input().split()
  X = int(X) #tempo necessario para completar o treinamento
  Y = int(Y) #tempo do trajeto de Super Buu
  K = 2 # X<Y 
  if (X>Y): # X <= Y*K
    # K >= X/Y : K = menor inteiro maior ou igula (X/Y) = função teto
    K = math.ceil(X/Y)
  print(K) # quantidade de segundos que se passa dentro da sala durante 1 segundo fora da mesma