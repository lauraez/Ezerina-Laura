f = open('dati2.txt','w', encoding='utf-8')

pilsetas = ['Sigulda ','Rīga ','Cēsis ']
f.writelines(pilsetas) # ieraksta vairākas rindiņas

# pārrakstīt faila saturu uz 3 valstīm

f = open('dati2.txt','w',encoding='utf-8')
valstis = ['Latvija ','Somija ','Lietuva ']
f.writelines(valstis)

"""#pārrakstīt faila saturu uz 3 valstīm
f = open('dati2.txt','w',encoding='utf-8')
valstis = {
    'Daugavpils':'Latvija',
    'Čitagonga':'Bangladeša',
    'Vladivostoka':'Krievija'
}
for object in valstis:
    f.write(valstis[object]+'\n')"""