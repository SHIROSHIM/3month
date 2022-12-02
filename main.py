viper = 'яуюоеёэиыУЕЁАОЭЯИЮAEIOUYaeiouy'
jett = 'БПГДХРЖКСЧЩЙЦЛШЩбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz '

while True:

    key = input('\nВведите предложение ')



    if key == 'выход':
        print('программа завершена')
        break

    g = 0
    s = 0
    for j in key:
        for w in jett:
            if j in w:
                g = g + 1

    for w in key:
        for f in viper:
            if w in f:
                s = s + 1

    g_total = g / len(key) * 100
    s_total = s / len(key) * 100

    print(f'количество букв {len(key)}')
    print(f'гласные: {s} согласные: {g} ')
    print(f'%:{round (s_total,2 )}% %:{round (g_total,2)}  ')
