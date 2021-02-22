from time import sleep
print('-='*20)
print(F'{"CONVERSÃO DE TEMPERATURAS":^40}')
print('-='*20, '\n')

opção = int(input('''[ 1 ] Celsius para Fahrenheit
[ 2 ] Fahrenheit para Celsius
[ 3 ] Celsius para Kelvin
[ 4 ] Kelvin para Celsius
[ 5 ] Fahrenheit para Kelvin
[ 6 ] Kelvin para Fahrenheit

Escolha sua opção: '''))

if opção == 1:
    c = float(input('Informe o grau em Celsius: '))
    f = c*1.8+32
    print('Convertendo...')
    sleep(2)
    print(f'{c}ºC é igual a {f:.2f}ºF')

elif opção == 2:
    f = float(input('Informe o grau em Farenheit: '))
    c = (f - 32)/1.8
    print('Convertendo...')
    sleep(2)
    print(f'{f}ºF é igual a {c:.2f}ºC')

elif opção == 3:
    c = float(input('Informe o grau em Celsius: '))
    k = c + 273.15
    print('Convertendo...')
    sleep(2)
    print(f'{c}ºC é igual a {k:.2f}K')

elif opção == 4:
    k = float(input('Informe o grau em Kelvin: '))
    c = k - 273.15
    print('Convertendo...')
    sleep(2)
    print(f'{k}K é igual a {c:.2f}ºC')

elif opção == 5:
    f = float(input('Informe o grau em Farenheit: '))
    k = (f+459.67)/1.8
    print('Convertendo...')
    sleep(2)
    print(f'{f}ºF é igual a {k:.2f}K')

elif opção == 6:
    k = float(input('Informe o grau em Kelvin: '))
    f = k*1.8-459.67
    print('Convertendo...')
    sleep(2)
    print(f'{k}K é igual a {f:.2f}ºF')

else:
    print('OPÇÃO INVALIDA!')
print('\nPROGRAMA FINALIZADO COM SUCESSO!!')
