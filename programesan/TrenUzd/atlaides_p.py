import math
a = int(input('Ievadiet preču daudzumu : '))   # mainīgais a apzīmē preču daudzumu

if a<0 :
    print('Dati ievadīti nepareizi')
    exit()

b = float(input('Ievadiet preces cenu : '))   # mainīgais b apzīmē preces cenu
c = input('Ievadiet preces nosaukumu : ')     # mainīgais c apzīmē prežu nosakumu

atl0 = round(b*a,2)
atl1 = round(0.3*(b*a),2)
atl2 = round(0.4*(b*a),2)
atl3_1 = round(0.2*(b*a),2)
atl3_2 = round(0.5*(b*a),2)
atl4 = round(0.3*(a*b),2)
atl5 = round(math.floor(a/2)*b,2)

karte = input('Vai jums ir karte?(j/n)')

print('Preču cena x veikalā ar 30% atlaidi ir : ',atl1)
print('Preču cena z veikalā ar 40% atlaidi ir : ',atl2)

if karte == 'j':
    print('Preču cena y veikalā ar kartes atlaidi 50% ir : ',atl3_2)
else:
    print('Preču cena y veikalā bez kartes atlaides 20% ir : ',atl3_1)

if a>=3:
    print('Jums ir 3 vai vairāk preces! R veikalā jūsu preču cena ar 30% atlaidi ir : ',atl4 )
else:
    print('R veikalā jums nav atlaižu! Jūsu preču cena ir : ',atl0)

if math.floor(a/2) >0:
    print('Jums katra otrā prece ir par brīvu! Jūsu preču cena H veikalā ir : ',atl5)
else:
    print('Jūsu preču cena H veikalā ir : ',atl0)