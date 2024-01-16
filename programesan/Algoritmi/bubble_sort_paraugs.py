''' programma ļauj lietotājam ievadīt skaitļus,
pēc tam tos sakārto ar burbuļkārtošanu'''
# izaicinājums tajā paša programma uztaisīt f-ju quicksort un selectionsort
#papildināt noformēt pēc saviem ieskatiem
def burbulis(saraksts):
    elementi = len(saraksts)# kopējais elemtu skaits
    for i in range(elementi):
        for j in range(0, elementi-i-1): #elements peld uz augsu, nonākot pareizajā vietā
            #izlaiž pēdējo(sakārtoto) elementu
            if saraksts[j]>saraksts[j+1]: # ja patiess tad notiek apmaina
                saraksts[j],saraksts[j+1]=saraksts[j+1],saraksts[j]
def sakartot():
    elementi = int(input('Ievadiet skaitļus cik būs sarakstā:\n'))
    saraksts = []
    for i in range(elementi):
        skaitlis = int(input(f'Ievadiet {i+1}.skaitli: '))
        saraksts.append(skaitlis)

    burbulis(saraksts) #tiek sakārtots
    print('Sakārtots saraksts:')
    for skaitlis in saraksts:
        print(skaitlis, end=' ')
sakartot()