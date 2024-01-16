augumi = {}
augumi['persona'] = ['persona1','persona2','persona3','persona4','persona5','persona6','persona7','persona8','persona9','persona10','persona11','persona12']
augumi['augums'] = [172,185,164,184,162,164,165,167,177,184,165,180]
print('(Dati augumiem ir centimetros)')
print(augumi)
while True:  
                     #programma turpināsies līdz netiks uzspiests 3 kas iziet no programmas
    darbiba = input('Ko jūs vēlaties darīt? 1-pievienot datus, 2-izdzēst datus, 3-iziet no programmas: ')
    # tā kā pēc katras darbības tiek parādīts viss saraksts ar personam un viņu augumiem nav vajadzības dot izvēli parādīt datus
    darbiba_atb = int(darbiba)
    if darbiba_atb == 3:  
        exit('Jūs izvēlējāties iziet no programmas.')
    elif darbiba_atb == 1:  # ja lietotājs izvēlas 1- pievienot datus lietotājam ir iespēja pievienot datus
        print('Jūs izvēlējaties pievienot klāt datus.')
        persona = input('Ievadiet personu: ')
        augums = input('Ievadiet šīs personas augumu(cm): ')
        augumi['persona'].append(persona) # sarakstā pie personam tiek pielikta klāt jaunā vērtība ko lietotājs ievadījis
        augumi['augums'].append(augums)   # sarakstā pie auguma tiek pielikta klāt jaunā vērtība ko lietotājs ievadījis
        print(augumi)
    elif darbiba_atb == 2:  # ja lietotājs izvēlas 2-izdzēst datus lietotājs var izdzēst datus
        print('Jūs izvēlējāties izdzēst datus.')
        persona = input('Ievadiet kuras personas datus jūs vēlaties izdzēst. ')
        index = augumi['persona'].index(persona)  #atrod personai attiecīgo augumu
        augumi['persona'].pop(index)  # no saraksta izvēlētā persona tiek izdzēsta
        augumi['augums'].pop(index)   # no saraksta tiek atrasts un izdzēsts attiecīgais augums izvēlētajai personai
        print(augumi)
