
finieris_laukums = 125*250  # lielumi tika mainīti no mm uz cm
podesta_standartizmers = 200*100
listes = 12
sturi = 8 

def materialuAprekins(garums,platums,augstums,skaits):
    podesta_laukums = garums * platums
    podesta_listes = ((podesta_laukums / podesta_standartizmers) * listes *skaits) - 12  # tika aprēķināts cik līstes ir vajadzīgas lai savienotu podestus
    podesta_sturi = skaits * sturi
    finiera_daudzums = (podesta_laukums / finieris_laukums)*skaits*10
    print('Jūs pasūtījāt podestu ar garumu ',garums,'cm, ar platumu ',platums,'cm, ar augstumu ',augstums,'cm')
    print('Nepieciešamais finiera daudzums ir ', finiera_daudzums)
    print('Nepieciešamais līstu skaits ir ', podesta_listes)
    print('Nepieciešamais skaits stūru savienojumu ir', podesta_sturi)


materialuAprekins(float(input('Podesta garums cm : ')),float(input('Podesta platums cm : ')),float(input('Podesta augstums cm : ')),int(input('Podestu skaits : ')))


def finiera_tips(koks):   # šī funkcija pārbaudīs kāda koka finieris ar noteiktu biezumu maksās
    if koks == 'egle':    # pārbauda kāds koks tika ievadīts
        e = int(input('kāds ir finiera biezums ( 12 / 15 / 18 / 21 (mm)): '))
        print(e)
        if e == 12:  # pārbauda kāds koka biezums tika ievadīts
            finiera_izmaksas = 68.50
        elif e == 15:
            finiera_izmaksas = 78.00
        elif e == 18:
            finiera_izmaksas = 86.50
        elif e == 21:
            finiera_izmaksas = 97.00
        print('par visu kopā jums būs jāsamaksā  : ',finiera_izmaksas*finiera_daudzums+podesta_listes*0.17+podesta_sturi*1.00)
    elif koks == 'priede':
        p = int(input('kāds ir finiera biezums ( 12 / 18 (mm)): '))
        print(p)
        if p == 12:
            finiera_izmaksas = 75.22
        elif p == 18:
            finiera_izmaksas = 99.18
        print('par visu kopā jums būs jāsamaksā  : ',finiera_izmaksas*finiera_daudzums+podesta_listes*0.17+podesta_sturi*1.00)
    elif koks == 'bērzs BB/WG':
        b_BB = int(input('kāds ir finiera biezums ( 12 / 15 / 18 / 21 (mm)): '))
        print(b_BB)
        if b_BB == 12:
            finiera_izmaksas = 57.39
        elif b_BB == 15:
            finiera_izmaksas = 65.30
        elif b_BB == 18:
            finiera_izmaksas = 74.75
        elif b_BB == 21:
            finiera_izmaksas = 85.99
        print('par visu kopā jums būs jāsamaksā  : ',finiera_izmaksas*finiera_daudzums+podesta_listes*0.17+podesta_sturi*1.00)
    elif koks == 'bērzs WG/WG':
        b_WG = int(input('kāds ir finiera biezums ( 12 / 15 / 18 / 21 (mm)): '))
        print(b_WG)
        if b_WG == 12:
            finiera_izmaksas = 53.08
        elif b_WG == 15:
            finiera_izmaksas = 60.40
        elif b_WG == 18:
            finiera_izmaksas = 67.00
        elif b_WG == 21:
            finiera_izmaksas = 76.89
        print('par visu kopā jums būs jāsamaksā  : ',finiera_izmaksas*finiera_daudzums+podesta_listes*0.17+podesta_sturi*1.00)

finiera_tips(input('kādu tipa finiri jūs vēlaties ( egle / priede / bērzs BB/WG / bērzs WG/WG ): '))