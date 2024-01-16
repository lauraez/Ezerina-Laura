name = 'Anna'
teksts = 'teksts'
skaitlis = 9  #skaitlis ir skaitlis ja nav pedins
print(name)  #rakstit nosaukumu kuru grib izdrukat
print(skaitlis)

#mainigo apvienosana
kombo = name, teksts  
print(kombo)

print('teksts var būt ar garumzīmēm,','bet mainīgajiem neliec garumzīmes')

#atrast vārda garumu
varda_garums = len(name)
print(varda_garums)

#chained_assingment = kaskādes veida piešķiršana
a = b = c = 300
print(a, b, c)

a, b = 10, 'hello'
print(a)
print(b)

#uzd1
masina = 'Volvo'
x = 50

x, y = 5, 10
print(x + y)

z = x + y
print(z)
