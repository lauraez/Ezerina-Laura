# ar inicializācijas virkni
# key:value   ir pāris      join noņem iekavas
'''dd = {'četri':(4,'four'), 'divi':(2,'two'), 'trīs':(3,'three')} # izveido sev jaunu vārdnīcu
print(dd)  # izdrukā vārdnīcu
print(len(dd))  # atgriež vārdnīcas garumu
print(dd.keys()) # atgriež atslēgas'''

#fromkeys metode vārdnīcas izveidošanai
dati = ('viens','divi','trīs')
vertiba = input('Vērtība:')
vardnica = dict.fromkeys(dati,vertiba)
print(vardnica)
