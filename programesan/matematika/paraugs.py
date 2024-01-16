import math     # raksta programmas saakumaa tikai vienu reizi

sk = 21.6

print('Noapaļots uz leju:', math.floor(sk))   # noapalo uz leju
print('Noapaļot uz augšu:', math.ceil(sk))    # noapaļo uz augšu

print('PI vērtība:', math.pi)   # atgrieš PI vērtību
print(math.pow(sk,3))     # kāpina skaitli 3. pakāpē

# Skaitlu formateesana

x = 252463/213
print('Bez formatēšanas',x)
print('Ar formatēšanu 1:',"%.2f"%x)
print('Ar formatēšanu 2: ' '{:.2f}'.format(x))