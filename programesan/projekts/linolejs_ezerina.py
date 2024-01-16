import math
linoleja_cena = float(input('Ievadiet linoleja cenu euro (0.00): '))
if linoleja_cena <0:
    exit('Datu ievadē ir notikusi kļūda, tika ievadīti negatīvi dati.')
rulla_platums = int(input('Ievadiet linoleja ruļļa platumu(m): '))
if rulla_platums <0:
    exit('Datu ievadē ir notikusi kļūda, tika ievadīti negatīvi dati.')
telpas_laukums = float(input('Ievadiet telpas laukumu(m2): '))

daudzums= math.ceil(telpas_laukums/rulla_platums)
daudzums_ist=telpas_laukums/rulla_platums
izmaksa = round(daudzums*linoleja_cena,2)
parpalikums =round(daudzums - daudzums_ist,2)

atb = input('Vai jūs vēlaties ieklāt apakšklāju? (j/n)')
if atb == 'n':
    print('---')
    print('Jūs nevēlaties ieklāt apakšklāju.')
elif atb == 'j':
    apakskl_cena = float(input('Ievadiet apakšklāja materiāla cenu euro (0.00)'))
    izmaksa_apaks = round(daudzums*apakskl_cena,2)
else:
    exit('Tāda nebija opcija')

if atb == 'n':
    print('---')
    print('Jums vajadzēs',telpas_laukums,'m2 linoleja jūsu telpai')
    print('---')
    print('Jums būs vajadzīgs nopirkt',daudzums,'linoleja kas maksās',izmaksa,'Eur')
    print('---')
    print('Jums paliks pāri',parpalikums,'m2 linoleja')
    print('---')
    print('Kopā:',izmaksa,'euro')
    print('---')
else:
    print('---')
    print('Jums vajadzēs',telpas_laukums,'m2 linoleja un apakšklāja jūsu telpai')
    print('---')
    print('Jums būs vajadzīgs nopirkt',daudzums,'linoleja kas maksās',izmaksa,'Eur')
    print('---')
    print('Jums būs vajadzīgs nopirkt apakšklāju kas maksās',izmaksa_apaks,'Eur')
    print('---')
    print('Jums paliks pāri',parpalikums,'m2 linoleja')
    print('---')
    print('Kopā:',izmaksa + izmaksa_apaks,'euro')
    print('---')