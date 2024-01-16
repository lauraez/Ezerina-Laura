
atbilde = 'n'
while atbilde == 'n':
    import math
    veikals = input('Kādā veikalā jūs iepērkaties?(Y/Z/X/R/H)')
    a = int(input('Ievadiet preču daudzumu : '))   # mainīgais a apzīmē preču daudzumu

    if a<=0 :                                   # pārbauda vai preču daudzums ir mazāks par nulli
        print('Dati ievadīti nepareizi')
        exit()

    b = float(input('Ievadiet preces cenu : '))   # mainīgais b apzīmē preces cenu
    c = input('Ievadiet preces nosaukumu : ')     # mainīgais c apzīmē preču nosakumu

    atl0 = round(b*a,2)
    atl1 = round((b*a)-(0.3*(b*a)),2)
    atl2 = round((b*a)-(0.4*(b*a)),2)
    atl3_1 = round((b*a)-(0.2*(b*a)),2)
    atl3_2 = round((b*a)-(0.5*(b*a)),2)
    atl4 = round((b*a)-(0.3*(a*b)),2)
    atl5 = round((b*a)-(math.floor(a/2)*b),2)

    karte = input('Vai jums ir karte?(j/n)')
    atbilde = input('Vai ir nopirkts viss, kas sarakstā?(j/n)')
if veikals == 'X':
    print('-----Čeks-----')
    print('Preču cena ar 30% atlaidi ir : ',atl1,'EUR')
elif veikals == 'Y':
    if karte == 'j':
        print('-----Čeks-----')
        print('Preču cena ar kartes atlaidi 50% ir : ',atl3_2,'EUR')
    else:
        print('-----Čeks-----')
        print('Preču cena bez kartes atlaides 20% ir : ',atl3_1,'EUR')
elif veikals == 'Z':
    print('-----Čeks-----')
    print('Preču cena ar 40% atlaidi ir : ',atl2,'EUR')
elif veikals == 'R':
    if a>=3:
        print('-----Čeks-----')
        print('Jums ir 3 vai vairāk preces! Jūsu preču cena ar 30% atlaidi ir : ',atl4,'EUR' )
    else:
        print('-----Čeks-----')
        print('R veikalā jums nav atlaižu! Jūsu preču cena ir : ',atl0,'EUR')
elif veikals == 'H':
    if math.floor(a/2) >0:
        print('-----Čeks-----')
        print('Jums katra otrā prece ir par brīvu! Jūsu preču cena ir : ',atl5,'EUR')
    else:
     print('-----Čeks-----')
     print('Jūsu preču ir : ',atl0,'EUR')
else:
    print('?')


