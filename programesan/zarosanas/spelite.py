import random
gajieni = ['akmens','papirs','skeres']

cilveka_gajiens = input('Ievadi savu gajienu: ')
datora_gajiens = random.choice(gajieni)

print(f'cilveks:{cilveka_gajiens} vs. dators: {datora_gajiens}')
if cilveka_gajiens == datora_gajiens:
    print('neizšķirts..')
elif cilveka_gajiens == 'akmens' and datora_gajiens == 'skeres':
    print('you win..')
elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens':
    print('you win..')
elif cilveka_gajiens == 'skeres' and datora_gajiens == 'papirs':
    print('you win..')
else:
    print('dators uzvar..')