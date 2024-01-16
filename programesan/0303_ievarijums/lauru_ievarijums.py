import math
izvele=input("Vai tu vēlies vārīt ievārījumu, pēc savas receptes? \n3kg āboli\n1kg cukurs\n500ml ūdens\n1 gab cirons\n1ml mandeļu ekstrakts\n10g kanēļa (j/n)\n")
if izvele=="n":
    print("atā")
    exit()
#1 kg cukura = 1,25 eiro, 1 citrona cenu = 29 centi, 59ml mandeļu ekstrakts = 6,73 eiro, 15 g kanēlis = 39 centi
abolusvars=float(input("Cik kg ābolu Jums ir?"))
#vajadzīgos daudzumus dalījām ar 3, lai iegūtu recepti 1 kg ābolu
cukurs=round(abolusvars*0.333,2)
udens=round(abolusvars*167,2)
citrons=round(1/3*abolusvars,2)
mandeles=round(abolusvars*1.67,2)
kanelis=round(abolusvars*3.33,2)
preces=["kg cukurs", " gab citrons", "ml mandeļu ekstrakts", "g kanelis"]
masas=[cukurs, citrons, mandeles, kanelis]
pakas=[1, 4, 59, 15]
def aprekini(x,y):
    x*y


#kods pajautā par katru no precēm
for i in preces:
    daudzums=float(input(f"cik daudz {i} tev ir mājās? "))
if daudzums<0:
        print("nepareizi dati")+exit()
elif daudzums<:
    print(f"Ej uz veikalu, jo tev pietrūkst {nepieciesams()} {i}") 
#ja preces ir mazak kā nepieciesams, jaiet uz veikalu
#for h in pakas:
    #def nepieciesams():
        #math.ceil((j-daudzums)/h)

    #for j in masas:
        #if daudzums<j:
            

