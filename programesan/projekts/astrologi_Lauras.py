import random # tiek ieviests random lai to varētu izmantot tālāk programmā
zimes = ['Auns','Vērsis','Dvīņi','Vēzis','Lauva','Jaunava','Svari','Skorpions','Strēlnieks','Mežāzis','Ūdensvīrs','Zivis'] # saraksts ar visām horoskopa zīmēm
sferas = ['mīlestības','naudas','veiksmes','veselības','darba','draudzības','ģimenes'] # saraksts ar visām pieejamām sfērām
print('Pieejamās sfēras:')
for sfera in sferas: # ar for ciklu visas saraksta vērības tiek izprintētas bez iekavām un komatiem
    print(sfera,end=', ') # saraksta vērtības tiek izprintētas viena pēc otras rindiņa un tās atdala komats
sfera = input('\nPar kuru sfēru būs visas prognozes, izvēlies no piedāvātajām (raksti ievērojot piemēru.):\n')
def teikumu_veidosana (teikums): # tiek izveidota funkcija ar vienu argumentu
    file= open(teikums,'r', encoding='UTF-8') # attiecīgais fails tiek atvērts lasīšanai
    rand_teikums = file.readlines() # tiek izlasītas rindiņas no faila
    rand_teikums_ir = random.choice(rand_teikums).replace('(sferas)',sfera) # programma izvēlas nejaušu rindiņu no faila 
    print(rand_teikums_ir.replace('\n','')) # no šīs rindiņas tiek izņemts \n
if sfera == sferas[0] or sfera == sferas[1] or sfera == sferas[2] or sfera == sferas[3] or sfera == sferas[4] or sfera == sferas[5] or sfera == sferas[6]: #nosacījumā ja lietotājs ir ievadījis sfēru pareizi nekas nenotiek
    print()
else: #nosacījumā ja lietotājs ir ievadījis sfēru nepareizi tad viņš tiek izsviests no programmas ar exit()
    exit('Dati ievadīti nepareizi. Jūs tiekat izsviests no programmas.')
def prognozes (): #tiek izveidota funkcija kas saliek visus teukumus kopā
    print('- - - - - Horoskopi šai nedēļai! - - - - -')
    for zime in zimes: # no sarksta ar horoskopa zīmēm ar for ciklu tiek atlasīta katra vērtība un katrai vērtībai tiek izpildīta tālākā funkcija
        print('----------')
        print(zime,'\n')
        teikumu_veidosana("prognozes_sakums_Lauras.txt")
        teikumu_veidosana("prognozes_vidus_Lauras.txt")
        teikumu_veidosana("prognozes_beigas_Lauras.txt")
    print('----------')
prognozes() # tiek izsaukta funkcija kas izsauc visas pārējās funkcijas