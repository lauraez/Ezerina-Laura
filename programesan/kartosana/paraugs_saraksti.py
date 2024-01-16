"""
darzeni = ['zirņi','burkāni','kartupeļi','batātes','gurķi']
print('Original saraksts:',darzeni)
darzeni.sort()
print('Sakartots saraksts:', darzeni)

viens = [6,8,3,100,9,69,1,-90]
print('Original saraksts:',viens)
print('Sakartots saraksts:',sorted(viens))

darzeni_kartots = sorted(darzeni,reverse=True)
print(darzeni)
print('apgriezts',darzeni_kartots)
"""
"""
saraksts = ['viens','divi','trīs','pieci','septiņi','deviņi']
saraksts_aug = sorted(saraksts,key=len) # pēc vārda garuma augoša secībā
saraksts_dilst = sorted(saraksts,key=len,reverse=True) # pēc vārda garuma dilstošā secībā
print(saraksts_aug)
print(saraksts_dilst)
"""

strs = ['rīts', 'Vakars', 'pusdienas', 'KOMPLEKSIŅŠ','ZEMENES']
strs.sort() # nestrādā printt funkcijā

print(strs)
print(sorted(strs,key=str.lower)) # ignores uppercase
print(sorted(strs,key=str.upper)) # ignores lowercase