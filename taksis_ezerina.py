dien = 0.57    #
nakt = 0.67       #
nol = 1.25           # mainīgajiem piešķir vērtības šajā gadijumā visas cenas
izs = 2.20        #
gaid = 0.13    #


print('Pasazieru skaits. (ievadīt skaitu)')
pas = int(input())     #   ar input funkciju lietotājs var pats ievadīt datus.  int pirms input norāda ka ka ievadīti dati būs skaitlis
if pas>4:      
    print('Pārāk daudz pasažieru')
    exit()             # exit funkcija pārtrauc programmu
elif pas<0:
    print('Ievadi pareizus datus')
    exit()

print('Cikos jūs savākt?(ja ir 15.00 tad rakstiit 15)')
laik = int(input())
if laik >= 24:         # if ir kā nosacījums šajā gadijumā ja laiks ir vienāds vai lielāks par 22 maksa par 1km būs nakts kas ir 0.67
    print('Ievadi pareizus datus')
    exit()
elif laik >= 22:         
    x = nakt           # mainīgajam iedot datus attiecīgi pēc nosacījuma izpildes
elif laik < 6 :        # elif ir kā nosacījuma turpinājums 
    x = nakt
elif laik >= 24:
    print('Ievadi pareizus datus')
    exit()
elif laik < 0:
    print('Ievadi pareizus datus')
    exit()
else:                  # nosacījuma beigas kas notiek ja tiek ievadīti visi nenosacītie dati
    x = dien

print('Vai mūsu firmas stāvvietā ir taksis? (j/n)')
stavv = input()        # šeit pirms input neliek int jo atbilde nebūs skaitlis
if stavv == 'j':
    b = nol
elif stavv == 'n':
    b = nol+izs        # mainīgajam b iedod divu citu mainīgo vērtību summu
else:         
    print('Ievadi pareizus datus')
    exit()

print('Cik ilgi jūs gaidīja ceļa laikā?(ievadīt skaitu minūtēs)')
gaid_laik = int(input())
if gaid_laik <0:
    print('Ievadi pareizus datus')
    exit()
else:
    k = gaid_laik*gaid  # mainīgajam k iedod divu citu mainīgo vērtību reiznājumu
    c = round(k, 2)     # mainīgo k noapaļo līdz diviem cipariem aiz komata

print('Cik tāls būs ceļš?(ievadīt skaitu km)')
attal = int(input())
if attal <= 0:
    print('Ievadi pareizus datus')
    exit()
else:
    l = x*attal
    d = round(l, 2)   # mainīgo l noapaļo līdz diviem cipariem aiz komata

bcd = round(d+b+c,2)
print('---------------- Č E K S ----------------')
print('* Maksa par nolīgšanu --',b,'EUR')
print('* Maksa par gaidīšanu --',c,'EUR')
print('* Maksa par km --', x,'EUR')
print('* Maksa par braukšanas garumu --',d,'EUR')
print('-----------------------------------------')
print(' Summa --',bcd,'EUR')
print('-----------------------------------------')
print('     Paldies ka izvēlējāties mūs! :)')
print('-----------------------------------------')
