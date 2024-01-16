import math
izvele=input("Vai tu vēlies vārīt ievārījumu, pēc savas receptes? \n3kg āboli\n1kg cukurs\n500ml ūdens\n1 gab cirons\n1ml mandeļu ekstrakts\n10g kanēļa (j/n)\n")
if izvele=="n":
    print("atā :)")
    exit()
#1 kg cukura = 1,25 eiro, 1 citrona cenu = 29 centi, 59ml mandeļu ekstrakts = 6,73 eiro, 15 g kanēlis = 39 centi
abolusvars=float(input("Cik kg ābolu Jums ir?"))
#vajadzīgos daudzumus dalījām ar 3, lai iegūtu recepti 1 kg ābolu
cukurs=round(abolusvars*3/3,2)
udens=round(abolusvars*500/3,0)
citrons=round(1/3*abolusvars,1)
mandeles=round(abolusvars*5/3,0)
kanelis=round(abolusvars*10/3,0)
print(f"Ar šādu ābolu svaru, Jums būs vajadzīgs: {cukurs}kg cukura, {udens}ml ūdens, {citrons}gab citrons, {mandeles}ml mandeļu ekstrakta, {kanelis}g kanēļa")
cukuri=input(f"Vai tev ir pietiekami daudz cukura? (j/n)")
udeni=input(f"Vai tev ir pietiekami daudz udens? (j/n)")
citroni=input(f"Vai tev ir pietiekami daudz citronu? (j/n)")
mandelu=input(f"Vai tev ir pietiekami daudz mandeļu ekstrakta? (j/n)")
kanelu=input(f"Vai tev ir pietiekami daudz kanēļa? (j/n)")
if cukuri=="n":
    omescukurs=float(input("Cik kg cukura tev ir?"))
    print(f"Ej pēc {cukurs-omescukurs}kg cukura")
if udeni=="n":
    omesudens=float(input("Cik ml ūdens tev ir?"))
    print(f"Ej pēc {udens-omesudens}ml ūdens")
if citroni=="n":
    omescitroni=float(input("cik citroni tev ir?"))
    print(f"Ej pēc {citrons-omescitroni}citroniem")
if mandelu=="n":
    omesmandeles=float(input("Cik ml mandeļu ekstrakta tev ir?"))
    print(f"Ej pēc {mandeles-omesmandeles}ml mandeļu ekstrakta")
if kanelu=="n":
    omeskanelis=float(input("Cik g kanēļa tev ir?"))
    print(f"Ej pēc {kanelis-omeskanelis}g kanēļa")
    
