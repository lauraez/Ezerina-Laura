# int paarveidoshana par string (a un b saskaita)
# a un b kaa teksts tiek konkatenēti(concat)
a = 5
b = 7
print('skaitlis', a + b)  # int tipa mainiiigie tiek saskaitiiti
print('teksts', str(a)+str(b)) # kaa teksti tiek concat
a = str(a)
b = str(b)
print('teksts', a + b)

#str paarveidoshana par int 
s = '123'
t = '456'
print(s + t, type(s + t))

a = int(s) # virkni s paarveido par int tipa mainiigo
b = int(t) # virkni t paarveido par int tipa mainiigo
print(a + b, type(a + b))

#uzd
 
a = 5
print(a, type(a))
a = float(a)
print(a, type(a))
a = int(a)
print(a, type(a))
b = 123.0
b = int(b)
print(b, type(b))