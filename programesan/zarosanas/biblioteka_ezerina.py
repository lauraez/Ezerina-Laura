izd_nod = input('Vai tev ir izdevumi kurus neesi nodevis? (j/n)')


if izd_nod == 'n':
    izd_piep = input('Vai tas ir piepraīts izdevums?')
    if izd_piep == 'j':
        print('Izdevumu izsniedz uz 2 dienām')
    else:
        izd_zh=input('Vai vēlies žurnālu? (j/n)')
else:
    print('Izdevumu nesaņemsi')




#    print(izd_zh=input('Vai vēlies žurnālu? (j/n)'))
#elif izd_zh == 'j':
#    print('izsniedz uz 7 dienam')
#elif izd_zh == 'n':
#    print(p_stud=input('Vai esi students? (j/n)'))
#elif p_stud == 'j':
#    print('Izdevumu saņem uz 14 dienām')
#else:
#    print('Izdevumu izsniedz uz 28 dienām')




