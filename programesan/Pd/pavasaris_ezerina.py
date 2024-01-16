import math 
def zvaigznites(n): # tiek veidota funkcija kas noteiktu skaitu n pārvērš par zvaigznītēm un tās izprintē vienā līnijā
    print('*'*n)      
def virsraksts(): # tiek veidota funkcija kas izprintē virsrakstu un funkciju kas izprintē tai doto= zvaigznīšu skaitu
    print('Faktoriāla aprēķināšana')
    zvaigznites(55)
virsraksts() # pasauc funkciju
while True:  # cikls kas atkārtosies līdz notikumam kas padara šo ciklu par nepatiesu
    vesels_sk=int(input('Ievadiet pozitīvu skaitli(mazāku par 13): \n')) # mainīgais kuram piešķir vērtību lietotājs
    def faktorials(n):  # tiek veidota funkcija ar vienu mainīgo
        print(math.factorial(n))  # tiks aprēķināts faktoriāls ar izvēlēto mainīgo
    def tuksums():  # tiek veidota funkcija ar kuru tiek izlaistas 2 rindiņas
        print('\n')
    if vesels_sk <13:   # nosacījums ja vesels_sk ir mazāks par 13 tad...
        faktorials(vesels_sk) # tiek pasaukta funkcija faktorials() kur mainīgais n ir vienāds ar mainīgo vesels_sk kurš savu vērtību saņem no lietotāja ievadītā
    elif vesels_sk <0:  # nosacījums ja vesels skaitlis ir mazāks par nulli
        print('Skaitlim ir jābūt lielākam par 0!')
    else:  # ja neizpildās neviens no iepriekš minētajiem nosacījumiem
        print('Ievadītais skaitlis ir pārāk liels!')
    jaut_turp_darbu=input('Vai vēlaties turpināt darbu?(j-jā, citi taustiņi-nē)\n')
    if jaut_turp_darbu != 'j': #nosacījums ja mainīgais jaut_turp_darbu nav vienāds ar atbildi j(jā) tad...
        tuksums() # tiek pasaukta funkcija tuksums()
        exit('Paldies!') # un tiek 'izmests' no programmas
    elif jaut_turp_darbu == 'j': # nosacījums ja mainīgais jaut_turp_darbu ir vienāds ar j(jā) tad...
        tuksums() # tiek izprintētas divas tukšas rindiņas
    

