valstis = {                 # Tiek izveidota vārdnīca ar atslēgām kā valstu nosaukumieim, un vērtībām kā attiecīgās valsts iedzīvotāju skaitu
    'Indija' :1342950000,
    'ASV':328626000,
    'Krievija':146877088,
    'Meksika':126320000,
    'Etiopija':98665000,
    'Vjetnama':94660000,
    'Turcija':82003882,
    'Francija':66992000,
    'Taizeme':66323917,
    'Dienvidkoreja':51811167
}
while True:  # Funkcija turpināsies līdz tā tiek apstādināta
    izvele = input('stop - iziet no programmas(var pielietot jebkurā momentā)\n1 - Valstis un to iedzīvotāju skaits tiek parādīts uz ekrāna augošā secībā pēc valstu nosaukumiem.\n2 - Valstis un to iedzīvotāju skaits tiek parādīts uz ekrāna dilstošā secībā pēc valstu nosaukumiem.\n3 - Valstis un to iedzīvotāju skaits tiek parādīts uz ekrāna augošā secībā pēc valstu iedzīvotaju skaita.\n4 - Valstis un to iedzīvotāju skaits tiek parādīts uz ekrāna dilstošā secībā pēc valstu iedzīvotaju skaita.\n5 - Pievienot valstis un to iedzīvotāju skaitu.\n6 - Valstis un to iedzīvotāju skaits tiek parādīts uz ekrāna.\nKo vēlaties darīt? ')
    # \n - tekstu pārliek jaunā rindiņā
    if izvele == 'stop':  # nosacījums - ja izvēle būs stop tad tiks izpildīti tālākie nosacījumi līdz nosacījuma beigām
        print('---')
        exit('Jūs izgājāt no programmas. Jauku jums dienu!')   # exit() iziet no programmas
        print('---') ##### (nosacījuma beigas)
    elif izvele == '1':
        print('---')
        print('Jūs izvēlējāties 1 \nValstis un to iedzīvotāju skaits tiek parādīts uz ekrāna augošā secībā pēc valstu nosaukumiem.')
        print('---')
        for i in sorted(valstis):   # sorted() - sakārto vārdnīcau augošā secībā   for i in - izvelk vārdnīcas atslēgas
            print((i, valstis[i]))  # izprintē vārdnīcas atslēgas un to vērtības stabiņa uz leju pēc sorted
        print('---')
    elif izvele == '2':
        print('---')
        print('Jūs izvēlējāties 2 \nValstis un to iedzīvotāju skaits tiek parādīts uz ekrāna dilstošā secībā pēc valstu nosaukumiem.')
        print('---')
        for i in sorted(valstis,reverse=True):  # reverse=True - sarakstu kārto otrādi - dilstošā secībā
            print((i, valstis[i]))
        print('---')
    elif izvele == '6':
        print('---')
        print('Jūs izvēlējāties 6 \nValstis un to iedzīvotāju skaits tiek parādīts uz ekrāna.')
        print('---')
        for i in valstis:
            print((i, valstis[i]))
        print('---')
    elif izvele == '5':
        print('---')
        print('Jūs izvēlējāties 5 \nPievienot valstis un to iedzīvotāju skaitu.')
        print('---')
        valsts_nosaukums = input('Ieraksti valsts nosaukumu(bez mīkstinājumiem un garumzīmēm):') # jauns mainīgais atslēgai - lai ievadtu jaunu valsti
        if valsts_nosaukums == 'stop':  # lai varētu izmantot stop funkciju jebkurā momentā
            print('---')
            exit('Jūs izgājāt no programmas. Jauku jums dienu!')
            print('---')
        iedz_sk = int(input('Ieraksti iedzīvotāju skaitu(stop nav pieejams):'))  # jauns mainīgais vērtībai - lai ievadītu šīs valstis iedzīvotāju skaitu. int() - lietotāja ievadītie dati ir skaitlis, funkcija nedarbosies ja ievadītie dati nebūs skaitlis
        valstis[valsts_nosaukums] = iedz_sk  # vārdnīcā valstis ieliek sarakstu valsts_nosaukums, kas ir atslēga, kuram pieder mainīgais iedz_sk(iedzīvotāju skaits), kas ir vērtība. 
        print("Atjaunotā vārdnīca:")
        print('---')
        for i in valstis:
            print((i, valstis[i]))
        print('---')
    elif izvele == '3':
        print('---')
        print('Jūs izvēlējāties 3 \nValstis un to iedzīvotāju skaits tiek parādīts uz ekrāna augošā secībā pēc valstu iedzīvotaju skaita.')
        print('---')
        kartots_iedz_sk = sorted(valstis,key=valstis.get)  # izveido jaunu mainīgo kas sakārto sarakstu pēc tā vērtībām
        kartota_valstis = {}  # izveido jaunu, tukšu sarakstu
        for key in kartots_iedz_sk:
            kartota_valstis[key] = valstis[key]
        for i in kartota_valstis:
            print((i, kartota_valstis[i]))
        print('---')
    elif izvele =='4':
        print('---')
        print('Jūs izvēlējāties 3 \nValstis un to iedzīvotāju skaits tiek parādīts uz ekrāna dilstošā secībā pēc valstu iedzīvotaju skaita.')
        print('---')
        kartots_iedz_sk = sorted(valstis,key=valstis.get,reverse=True)
        kartota_valstis = {}
        for key in kartots_iedz_sk:
            kartota_valstis[key] = valstis[key]
        for i in kartota_valstis:
            print((i, kartota_valstis[i]))
        print('---')
    else:   # ja ievada simbolu/s kas nav doti kā opcijas izpildās tālākais nosacījums
        print('---')
        print('Tāda opcija netika piedāvāta')
        print('---')
