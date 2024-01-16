#  uzrakstit programmu kura ir 2 saraksti ar + abus apvienot

mans_saraksts = ['svece', 2, 'sāls'] #  pirmais elements ir ar indeksu 0
tavs_saraksts = ['karstmaizes', 'brauniji','kafija']

liels_saraksts = mans_saraksts + tavs_saraksts
print(liels_saraksts)


#  nokopet saraksta vertibas un ievietot tas jauna saraksta

milzis = ['zupa', 'dzervene', 'tast']

jauns = list(milzis)

print(milzis)
print(jauns)


#  izveidot sarakstu ar chetriem kraasu nosaukumiem atrast katra elementa garumu

#  var 1

krasas = ['sarkans', 'zils', 'roza', 'violets']
jauns_saraksts = []        #  tukshs saraksts
for krasa in krasas:
    burti = 0   #  katru reizi palaizhot sarakstu, atgriezas uz 0
    for burts in krasa:
        burti +=1    #  katru reizi pieskaita 1
    pagaidu_saraksts = [krasa, burti]
    jauns_saraksts.append(pagaidu_saraksts)

print(jauns_saraksts)

#  kaa sho kodu var uztaisiit ar mazaak rindinaam? vai ir vienkaarshaaks veids kaa atrsast vaarda garumu?

#  var2

krasas = ['sarkans', 'zils', 'roza', 'violets']
for krasa in krasas:
    print(len(krasa))


# var 3

krasas = ['sarkans', 'zils', 'roza', 'violets']
jauns = []
for krasa in krasas:
    jauns.append([krasa, len(krasa)])

print(jauns)