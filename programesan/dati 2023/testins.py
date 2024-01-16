fails = open('ziema.txt','w',encoding='UTF-8')
# w- izveido neeksisteejosu failu no jauna
# ieraksta failaa datus
saraksts = ['Alūksne\n','Valmiera\n','Balvi\n']
fails.writelines(saraksts) # ieraksta vairākas rindiņas
fails.write('Es vēlos gulēt')
fails.close()

#pārrakstīt kopēta faila saturu
fails = open('ziema_copy.txt','w+',encoding='UTF-8')
fails.write('Varētu drīz iet pusdienās..')
# paraada faila saturu uz ekraana
fails = open('ziema_copy.txt','w+',encoding='UTF-8')
print(fails.read()) 
fails.close()

fails = open('ziema_copy.txt','a+',encoding='UTF-8')
fails.write('\nCerams pusdienas šodien būs garšīgas...')
fails.close()