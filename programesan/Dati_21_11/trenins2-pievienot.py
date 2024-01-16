#pievienosana ir a
file_name = 'dzest.txt'
teksts = 'New info'

try:
    with open(file_name,'a',encoding='UTF=8') as fails:
        fails.write('\n'+teksts)  
    print(f'Jauna informācija veiksmīgi pievienota failam "{file_name}".')
except FileNotFoundError:
    print(f'Kļūda: data {file_name} nav atrasts.')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')