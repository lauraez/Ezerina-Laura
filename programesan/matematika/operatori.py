print('Ievadiet trīs skaitļus:')
a = int(input())
b = int(input())
c = int(input())

#   loģiskais and
"""
if a>0 and b>0 and c>0:
    print('Visi skaitļi ir lielāki par nulli')
else:
    print('Vismaz viens skaitlis nav lielāks vai ir vienāds par nulli')
"""
# loģsikais or

if a>0 or b>0 or c>0:
    print('Viens skaitlis  ir lielāks par nulli')
else:
    print('Neviens skaitlis nav lielāks  par nulli')
