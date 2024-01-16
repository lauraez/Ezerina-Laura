file_name = 'dzest.txt'
delete_me = 'Drīz būs Ziemassvētku brīvdienas!'

try:
    with open(file_name,'r',encoding='UTF=8') as data:
        #r atver failu lasiishanai un sglabaa mainiigajaa data
    #readlines ielasa visas rindas no faila un saglabaa taas sarakstaa
        rows = data.readlines()

    with open(file_name,'w',encoding='UTF=8') as data: # atver rakstiisanai paarraksta
        for row in rows: # iteree cauri visaam saraksta rindaam
            if delete_me not in row:
                data.write(row)
    # ja neatrod vaardu tad sii rinda pieraksta so rindu atpakal failaa ignoreejot vai izdzeesos rindas kuras atbilst
    print(f'Rindas ar vārdu "{delete_me}" ir veiksmīgi dzēstas no faila "{file_name}".')
except FileNotFoundError:
    print(f'Kļūda: data {file_name} nav atrasts.')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')