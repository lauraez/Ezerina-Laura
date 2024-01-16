rezultatu_saraksts = {}
students = []
eksamena_rezultats = []
studentu_skaits = int(input('Cik daudz studentus jūs pierakstīsiet: '))
skaits = 0
while skaits<studentu_skaits:
    vards = input('Ievadiet studenta vārdu: ')
    rezultats = int(input('Ievadiet šī studenta eksamena rezultātu(no 0 līdz 100(vesels skaitlis)): '))
    students.append(vards)
    eksamena_rezultats.append(rezultats)  
    skaits=skaits+1

for key in students:
    for value in eksamena_rezultats:
        rezultatu_saraksts[key] = value
        eksamena_rezultats.remove(value)
        break
print(rezultatu_saraksts)
#print(sorted(rezultatu_saraksts.items(), key=lambda x:x[1]))