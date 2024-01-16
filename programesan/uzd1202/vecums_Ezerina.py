vecums = int(input('suņa vecums = '))
if vecums <0:
    print('nav')
elif vecums <=2:
    print ('suņa vecums cilvēka gados ir ',vecums*10.5)
elif vecums >2:
    print('suņa vecums cilvēka gados ir ',21+(vecums-2)*4)