import os

os.system('cls ')

print('----------PUTNO 1----------\n')
a = 5.5
b = 1
c = True
d = 'hola'
print('Variables: ',str(a),',',str(b),',',str(c),',',str(d))
print('',type(a),'\n',type(b),'\n',type(c),'\n',type(d))

print('\n\n----------PUTNO 2----------\n')
tup = (1,2,3,4,5,6,7,8,9)
z = len(tup)
print(str(' Tupla:'),str(tup))
print(' Primer Valor: ',str(tup[0]),'\n','Ultimo Valor: ',str(tup[z-1]))

print('\n\n----------PUTNO 3----------\n')
print('Tupla antes de agregar strings:',str(tup),'\n')
str1 = str(input('Ingrese primer String: '))
str2 = str(input('Ingrese segundo String: '))
str3 = str(input('Ingrese tercer String: '))
tup = tup + (str1, str2, str3)
print('\nTupla despues de agregar strings:',str(tup))

print('\n\n----------PUTNO 4----------\n')
while(True):
    print('Tupla:',str(tup),'\n\nQuieres verificar strings o numeros? (Escribe S o N):')
    x = str(input())
    if x == 'S':
        x = str(input('\nIngresa string a verificar (Caps sensitive): '))
        y = x in tup
        if y == True:
            print('\nSi esta en la tupla')
            exit()
        else:
            print('\nNo esta en la tupla')
            exit()
    elif x == 's':
        x = str(input('\nIngresa string a verificar (Caps sensitive): '))
        y = x in tup
        if y == True:
            print('\nSi esta en la tupla')
            exit()
        else:
            print('\nNo esta en la tupla')
            exit()
    elif x == 'N':
        x = int(input('\nIngresa numero a verificar: '))
        y = x in tup
        if y == True:
            print('\nSi esta en la tupla')
            exit()
        else:
            print('\nNo esta en la tupla')
            exit()
    elif x == 'n':
        x = int(input('\nIngresa numero a verificar: '))
        y = x in tup
        if y == True:
            print('\nSi esta en la tupla')
            exit()
        else:
            print('\nNo esta en la tupla')
            exit()
    else:
        print('Opcion no valida')