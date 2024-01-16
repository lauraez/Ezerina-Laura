darbu_saraksts = {}
darbu_saraksts ['daramais_darbs'] = []
darbu_saraksts ['termins'] = []

def darbu_pievienosana():
    while True:
        print('Jūs tagad pievienojat datus.')
        daramais_darbs = input('Jūsu darāmais darbs:\n')
        termins = int(input('Jūsu darba termiņš (dienu skaits vesels skaitlis):\n'))
        if termins <= 0:
            print('Jūs nedrīkstat ievadīt negatīvus skaitļus vai nulli.')
        elif termins > 0:
            darbu_saraksts ['daramais_darbs'].append(daramais_darbs)
            darbu_saraksts ['termins'].append(termins)
        parbaude = input('Vai vēlaties pievienot vēl datus? (y/n)\n')
        if parbaude == 'n':
            break
        elif parbaude =='y':
           continue
        else:
            print('Jūs ievadījāt nepareizo atbildi..')

darbu_pievienosana()
while True:
    izvele = int(input('Ko jūs vēlaties darīt: 1-pievienot darbu, 2-izdzēst darbu, 3-mainīt darba statusu, 4-sakārtot sarakstu, 5-eksportēt teksta failā, 6-apskatīt sarakstu, 7- iziet no programmas \n'))
    if izvele <= 0:
        print('Nav tādas opcijas.')
    elif izvele > 7:
        print('Nav tādas opcijas.')
    elif izvele == 1:
        darbu_pievienosana()
    elif izvele == 2:
        print('Jūs izvēlējāties izdzēst datus.')
        print(f'Jūsu esošais saraksts {saraksts}')
        daramais_darbs = input('Ievadiet kuru darāmo darbu jūs vēlaties izdzēst:\n ')
        index = darbu_saraksts['daramais_darbs'].index(daramais_darbs) 
        darbu_saraksts['daramais_darbs'].pop(index)  
        darbu_saraksts['termins'].pop(index)
    elif izvele == 6:
        print(darbu_saraksts)
    elif izvele == 7:
        exit('Jūs izvēlējāties iziet no programmas.')
    elif izvele == 5:
        f = open('darbu_saraksts.txt','w',encoding='utf-8')
        f.write(str(darbu_saraksts))
        f.close()
    elif izvele == 4:
        kartots = sorted(darbu_saraksts,key=darbu_saraksts.get)
        sara = {}
        for key in kartots:
            sara[key] = darbu_saraksts[key]
        print(sara)
    elif izvele == 3:
        daramais_darbs = input('Ievadiet kuru darāmo darbu jūs esiet pabeidzis:\n ')
        index = darbu_saraksts['daramais_darbs'].index(daramais_darbs)
        darbu_saraksts.update({})