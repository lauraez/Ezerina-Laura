print('Programmu izstrādāja: Laura Ezeriņa.')
print('')
print('Laukuma aprēķins ģeometriskām figūrām')
print(' ****')
print('Ievadiet malas A garumu:')

a = float(input())

print('Malas A garums:', a)
print(' ****')
print('Ievadiet malas B garumu:')

b = float(input())

print('Malas B garums:', b)
print(' ****')
print('Ievadiet augstumu:')

h = float(input())

print('Augstums:', h)

s_tri = a*h/2
s_tra = ((a+b)/2)*h
s_par = a*h

print('Laukums trijstūrim:', s_tri )
print('Laukums trapecei:', s_tra)
print('Laukums paralelogramam:', s_par)
print(' ****')
print('Paldies!')