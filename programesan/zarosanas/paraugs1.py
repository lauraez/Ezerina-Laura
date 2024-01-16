atbilde = input('Vai šodien ir tava dzimšanas diena?(j/n)')
if atbilde == 'j': #salidzinasana ir veicama ar divam vienadibas zimem
    print('Daudz baltu dieniņu!')

tests = input('Vai šodien ir jaungada diena?(j/n)')
if tests == 'j': 
    print('Laiks salūtam!')
else:  #pie else nosacījuma nebūs(tas ir tas kas paliek pāri)
    print('bēdīgi..') # šis tiek palaists tikai tad ja lietotājs neieraksta 'j'
