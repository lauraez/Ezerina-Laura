reiz = 7
for i in range(1,13,1):
    print('Cik ir',i,"x",reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break
    if minejums ==  'izlaist':
        print('Tiek izlaists')
        continue
    atb = i*reiz   #glabā pareizās atbildes
    if int(minejums) == atb:
        print('Pareizi')
    else:
        print('No tas ir ', atb)