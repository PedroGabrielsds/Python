#Aula 11 - Cores no Terminal
import colorsysx

#Padrão ANSI

#Padrão de cores - \033[Style;Text;BACKm

#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|
#|   Códigos de Style: 0, 1, 2, 4 e 7     |
#|    Style 0 - None                      |
#|    Style 1 - Bold                      |
#|    Style 4 - Underline                 |
#|    Style 7 - Negative                  |
#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|

#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|
#|     #Códigos de text: 30 até 37        |
#|       Text 30 - Black                  |
#|       Text 31 - Red                    |
#|       Text 32 - Green                  |
#|       Text 33 - Yellow                 |
#|       Text 34 - Blue                   |
#|       Text 35 - Purple                 |
#|       Text 36 - cyan                   |
#|       Text 37 - White                  |
#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|

#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|
#|    #Códigos de Background: 40 até 47   |
#|       Text 40 - Black                  |
#|       Text 41 - Red                    |
#|       Text 42 - Green                  |
#|       Text 43 - Yellow                 |
#|       Text 44 - Blue                   |
#|       Text 45 - Purple                 |
#|       Text 46 - cyan                   |
#|       Text 47 - White                  |
#|=--=--=--=--=--=--=--=--=--=--=--=--=--=|

print('\033[1;37;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[1;37;42mTeste\033[m')
print('\033[7mTeste\033[m')

print('\033[4;37;45mOlá, Mundo!\033[m')

print("\033[1;31;40mMack\033[m")

print(f"Olá \033[1;31;40mMack\033[m, seja bem vindo ao \033[1;34;43mPython\033[m!")