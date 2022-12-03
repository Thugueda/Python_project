import os
# Δ = b² - 4*a*c
# x = – b ± √Δ
#      2·a
os.system("pip install termcolor ")
os.system('pip install time')
os.system("cls")
os.system("clear")
from termcolor import colored
import time
print(colored('Obrigado por testar esse script', 'red', 'on_white'))
time.sleep(2)
r = 0
while r != 5:
    os.system("cls")
    os.system("clear")
    print(colored('''
      ██████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗ █████╗ ██████╗  █████╗
      ██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
      ██████╔╝███████║███████║███████╗█████╔╝ ███████║██████╔╝███████║
      ██╔══██╗██╔══██║██╔══██║╚════██║██╔═██╗ ██╔══██║██╔══██╗██╔══██║
      ██████╔╝██║  ██║██║  ██║███████║██║  ██╗██║  ██║██║  ██║██║  ██║
      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
      ''', 'cyan'))
    print(colored('Criado por Thugueda,\nInstagram -> xx_thu.gueda_xx', 'blue', 'on_white'))
    print('')
    a = int(input('Valor de A:   '))
    b = int(input('Valor de B:   '))
    c = int(input('Valor de C:   '))
    print('')
    # Delta inicio
    delta = b**2 - 4*a*c
    # Mostrar formula na tela
    print(colored('Δ = {}² - 4 x {} x {} = {}'.format(b, a, c, delta), 'blue'))
    print(colored('Δ = {} '.format(delta), 'cyan'))  # Valor de Delta
    print(colored('=-=-' * 10, 'green'))
    # delta fim

    if delta == 0:
        print(colored('''x = – ({}) - √{}
             2·{}'''.format(b, delta, a), 'cyan'))  # show shape on screen
        x = (-b - delta**0.5) / (2*a)  # Calcular
        print('A solução e de  [{:.0f}]'.format(x))  # resultado
        print(colored('=-=-' * 10, 'green'))
        o = input('aperte para reiniciar........')

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        print(colored('''x = + ({}) - √{}
             2·{}'''.format(b, delta, a), 'cyan'))
        print('=-=-' * 10)
        x2 = (-b - delta**0.5) / (2*a)
        print(colored('''x = – ({}) - √{}
             2·{}'''.format(b, delta, a), 'cyan'))
        print('=-=-' * 10,)
        print('Resolução = [{:.0f}/{:.0f}]= '.format(x1, x2))
        print('=-=-' * 10,)
        o = input('aperte para reiniciar........')
    if delta < 0:
        print(
            'Delta negativo\nA conta acaba aqui!\nResultado = {:.0f}'.format(delta))
        print(colored('=-=-' * 10, 'green'))
        o = input('aperte qualquer coisa para dar restart........')
