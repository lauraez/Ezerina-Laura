faila_nosaukums = 'mana_klase.txt'

# mēģināt atvērt failu un lasīt datus
try:
    with open(faila_nosaukums,'r',encoding='UTF-8') as fails:
        for rindina in fails:
            dati = rindina.split() #katru rindinu sadala pa vārdiem
            #parbaudit vai pietiek datu (vārds, uzvārds, vecums)
            if len(dati) >= 3:
                vards = dati[0]
                uzvards = dati[1]
                vecums = dati[2]

                print(f'Vārds:{vards}, Uzvards:{uzvards}, Vecums:{vecums}')
            else:
                print('Kļūda: nepietiekami daudz dati failā.')
except FileNotFoundError:
    print(f'Kļūda : Fails"{faila_nosaukums}"nav atrasts.')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')