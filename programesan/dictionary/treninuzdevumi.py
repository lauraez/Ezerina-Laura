# 1 uzd
telefoni = {
    'zīmols': 'Apple',
    'modelis': '14',
    'gads': 2021
}
telefoni.update({'gads':2023})
print(telefoni)

#2 uzd
skolas = {
    'nosaukums':'Gimnāzija',
    'novads':'Sigulda',
    'skolenu_skaits': 569,
    'gads': 2019
}
skolas.clear()
print(skolas)

#3 uzd
augli = {1:'banāni',2:'aboli',3:'bumbieri',4:'mango' }
print(augli)
augli.pop(1)
augli.pop(2)
print(augli)

# 4(3) uzd
skaitli = {'a':100,'b':200,'c':300,'d':400}
if 200 in skaitli.values():
    print('skaitlis 200 ir vārdnīcā!')