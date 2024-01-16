import math
import random

print('Ievadiet riņķa līnijas rādiusu:')
r = int(input())
print(float(r))

rlg = 2*math.pi*r
print('Riņķa līnijas garums:',"%.2f"%rlg)

rll = math.pi*math.pow(r,2)
print('Riņķa līnijas laukums:',"%.2f"%rll)


print('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:')
vk = int(input())

print('Ievadiet taisnleņķa trijstūra otrās katetes garumu:')
dk = int(input())


h = math.sqrt(math.pow(vk,2)+math.pow(dk,2))
print('Taisnleņķa hipotenūzas garums:',"%.2f"%h)

rand = random.random()
print('Gadījuma skaitlis no 0 līdz 1:', rand)