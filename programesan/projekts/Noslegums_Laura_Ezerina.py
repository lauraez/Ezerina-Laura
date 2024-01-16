from datetime import datetime
lists = [] # izveidoju tukšu sarakstu lai varētu padarīt to par global listu
def galvena(): #funkcija galvena() kurā notiek visas pārējās galvenās funkcijas
    print('---  ---  ---\nEsiet sveicināts, šeit jūs varēsiet pierakstīt savus eksperimentus!\n---  ---  ---')
    while True: # cikls kurā nav sveicināšanās lai tā nenotiek katru reizi. Viss kas ir while ciklā atkārtosies līdz nebūs break
        iegut_datus(str(input('Ievadiet jūsu eksperimenta nosaukumu!\n:')),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        str(input('Ievadiet jūsu vārdu vai uzvārdu! Atstarpes un mazais sākuma burts netiek ņemts vērā.\n:')),
        str(input('Ievadiet jūsu eksperimenta veikšanas vietu!\n:')))
        # 2. mainīgais 'laiks' ir funkcija datetime.now.strftime('%Y-%m-%d %H:%M:%S') ir tagadējais laiks kurš parādās kā gggg/mm/dd un ss,mm,ss šim ir vajadzīgs datetime import
        saglabat_datus()# tiek izsaukta funkcija kura ievieto eksperimenta datus .txt failā
        turpina = input('Vai jūs pievienosiet vēl eksperimentus?(j/n)\n:')
        if turpina == 'j':
            continue # atkārto while ciklu no sākuma
        elif turpina == 'n' or turpina=='exit' or turpina == 'stop' or turpina == 'iziet': # pārbauda lietotāja ievadītos datus 
            print('---  ---  ---\nJūs izvēlējāties iziet no programmas!\n---  ---  ---')
            break #pārtrauc ciklu
        else: #ja teik ievdīti nezināmi, negaidīti dati
            print('Ievadījāt nepareizus datus...\nJūs tiekat izsviests no programmas.')
            break
def iegut_datus(eksperimenta_nosaukums,laiks,vards,vieta): #funkcija ar četriem parametriem
    global lists #padara sarakstu ar nosaukumu lists par globālo sarakstu lai to varētu izmantot arī ārpus funkcijas
    lists = [eksperimenta_nosaukums,laiks,vards,vieta] # izveido personas ievadītos datus par sarakstu
    return
def pareizs_vards(): #funkcija kura mainīgo vards izlabo ar lielo burtu un bez atstarpēm
    lists[2]=lists[2].replace(" ","") # saraksta trešajai vērtībai tiek aizstātas atstarpes bez atstarpēm ar .replace() funkciju pirmā vērtība ir ko vēlas aizstāt otrā - ar ko vēlas aizstāt
    lists[2]=lists[2].capitalize() # saraksta otrās vērtības pirmais burts mazais vai lielais tiek pārvērsts par lielo
def saglabat_datus(): #funkcija kas pievieno un saglabā ierakstītos datus
    eksperimenta_dati = "eksperimenta_dati.txt" 
    pareizs_vards() #izsauc funkciju pareizs vards lai pirms teksta ievades teksta failā tas tiktu pārveidots pareizi
    try: #pārbauda un uztver kādas kļūdas vai neparedzējumus
        with open(eksperimenta_dati,'a',encoding='UTF-8') as fails: # atver txt failu ja tāds jau eksistē bet izveido ja neeksistē
            fails.writelines(f'\nEksperimenta nosaukums: {lists[0]}, datums un laiks {lists[1]}, vārds:{lists[2]}, vieta:{lists[3]}') #ieraksta vajadzīgo informāciju failā
        print(f'Jauna informācija veiksmīgi pievienota failam "{eksperimenta_dati}".')
    except FileNotFoundError: #Ja txt fails netiek atrasts tad izpildās tālākie nosacījumi
        print(f'Kļūda: data {eksperimenta_dati} nav atrasts.')
    except Exception as e: #Ja ir citas kļūdas vai neparedzējumi tad izpildās tālākie nosacījumi un šo "kļūdu" nosauc par mainīgo e
        print(f'Kļūda: neparedzēta kļūda - {e}')
galvena() # izsauc galveno funkciju 