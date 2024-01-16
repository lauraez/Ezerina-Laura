def pasuti_tkreklus(skaits,apdruka,piegade):  #Funkcija ar trīs parametriem
  if apdruka == "TEKSTS": #Ja apdruka ir izvēlēta kā TEKSTS
    parbaude_TEKSTS(skaits)  #izsauc funkciju kas pārbauda kreklus ar attiecīgi izvēlēto apdruku
  elif apdruka =="ZIME": #Ja apdruka ir izvēlēta kā ZIME
    parbaude_ZIME(skaits)
  elif apdruka =="FOTO": #Ja apdruka ir izvēlēta kā FOTO
    parbaude_FOTO(skaits)
  else:
    exit()# exit() funkcija pārtrauc programmu
def ceks_piegade(cena):  #funkcija kas aprēķina summu un izvada čeku ar piegādes cenu
    piegade = 15
    summa=cena+piegade
    print("---Čeks---")
    print("Summa:",summa,"EUR")
def ceks_bez_piegade(cena): # funkcija kas aprēķina summu un izvada čeku bez piegādes cenas
    piegade=0
    summa = cena+piegade
    print("---Čeks---")
    print("Summa:",summa,"EUR")
def ceks_atlaide(cena): #funkcija kas aprēķina summu un izvada čeku ar 5% atlaidi un bez piegādes cenas
    piegade = 0 
    procenti = (cena+piegade)*0.05 #aprēķina cik ir 5% no kreklu cenas summas
    summa = (cena+piegade)-procenti # aprēķina cik maksās krekli ar šo atlaidi
    print("---Čeks---")
    print("Jums nav jāmaksā par piegādi")
    print("tika piešķirta 5% atlaide")
    print("Summa:",summa,"EUR")
def parbaude_FOTO(skaits): # funkcija kas pārbauda foto apdrukāto kreklu skaitu un kreklu kopējo summu lai varētu izvadīt attiecīgo čeku
    if skaits>0:
      cena=20*skaits
      cenas(cena,skaits)
def parbaude_TEKSTS(skaits):# funkcija kas pārbauda teksta apdrukāto kreklu skaitu un kreklu kopējo summu lai varētu izvadīt attiecīgo čeku
    if skaits>0:
      cena=5*skaits
      cenas(cena,skaits)
def parbaude_ZIME(skaits):# funkcija kas pārbauda zīmes apdrukāto kreklu skaitu un kreklu kopējo summu lai varētu izvadīt attiecīgo čeku
    if skaits>0:
      cena=7*skaits
      cenas(cena,skaits)
def cenas(cena,skaits):
    if skaits <=0:
      exit()
    elif cena <50:
      ceks_piegade(cena)
    elif cena > 100:
      ceks_atlaide(cena)
    elif cena >= 50:
      ceks_bez_piegade(cena)
#Izsauc funkciju kurā lietotājs ievada datus
pasuti_tkreklus(int(input("Cik kreklus vēlies?")),input("Kuru apdrukas veidu tu vēlies?(TEKSTS/ZIME/FOTO)"),0)