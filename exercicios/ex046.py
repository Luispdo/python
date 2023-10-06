from time import sleep
import emoji
print('Contagem regressiva para os fogos!!!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1;33mVIVA!!!\033[m')
for c in range(0, 5):
    print(emoji.emojize(':fogos_de_artifício:', language='pt'))
    sleep(1)
