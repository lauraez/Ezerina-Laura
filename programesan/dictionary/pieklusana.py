#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']
}
#1 variants ar for ciklu
'''for atslega, vertiba in valstis.items():
    for i in vertiba:
        print('{}: {}'.format(atslega,i))
    print('-------------------------------')'''

# 2 variants ar for ciklu vienai atslēgu grpai
for i in valstis['Dānija']:
    print(i)

# iegūt pirmās 3 pilsētas no Somijas
print(valstis['Somija'][:3])

# iegūt pēdējās divas pilsētas no Norvēģijas
print(valstis['Norvēģija'][-2:])

# iegūt visas pilsētas no somijas izņemot pēdējas 3
print(valstis['Somija'][:-3])

#iegūt 2to līdz 5to pilsētu no Dānijas
print(valstis['Dānija'][1:5])

