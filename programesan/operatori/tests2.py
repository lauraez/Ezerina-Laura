#tiek realizeta decimalskaitlu ievade
#aprekinats izteiksmes (x+y)*(x-y)/x-y rezultats

print('Ievadiet savu vārdu:')
vards = input()
print('Juusu vards ir:', vards)

print('ievadiet decimalskaitli:')
x = float(input())     #javeic konvertesana jo input funkcijai datus atgriez teksta veida
print('ievadiitais skaitlis ir:', x)

print('ievadiet decimalskaitli:')
y = float(input())     #javeic konvertesana jo input funkcijai datus atgriez teksta veida
print('ievadiitais skaitlis ir:', y)


rezultats = (x+y)*(x-y)//(x-y)
print('rezultaats:', rezultats)
