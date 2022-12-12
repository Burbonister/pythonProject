import os

while True:
    sayt = input('Enter the site:')
    if sayt == ('stop'):
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')

    elif 'www. ' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        print('elif')

    else:
        sayt = 'https://www.' +sayt
        os.system('start ' +sayt)
        print('else')
