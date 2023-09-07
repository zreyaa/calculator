print("Wilkommen im dümmsten Rechner der Welt! Gemacht von mxZerra")


print('Wähle aus zwischen: ')
print('1. Addition')
print('2. Subtraktion')
print('3. Multiplikation')
print('4. Division')
operation = input()





def plus():
    zahl1 = int(input('Gebe eine Zahl ein: '))
    zahl2 = int(input('Gebe eine zweite Zahl ein: '))
    ergebnis = int(zahl1) + int(zahl2)
    print(str('Das Ergebnis ist ') + str(ergebnis))
    input('Drücke ENTER zum Beenden.')

def minus():
    zahl1 = int(input('Gebe eine Zahl ein: '))
    zahl2 = int(input('Gebe eine zweite Zahl ein: '))
    ergebnis = int(zahl1) - int(zahl2)
    print(str('Das Ergebnis ist ') + str(ergebnis))
    input('Drücke ENTER zum Beenden.')

def mal():
    zahl1 = int(input('Gebe eine Zahl ein: '))
    zahl2 = int(input('Gebe eine zweite Zahl ein: '))
    ergebnis = int(zahl1) * int(zahl1)
    print(str('Das Ergebnis ist ') + str(ergebnis))
    input('Drücke ENTER zum Beenden.')

def geteilt():
    zahl1 = int(input('Gebe eine Zahl ein: '))
    zahl2 = int(input('Gebe eine zweite Zahl ein: '))
    ergebnis = int(zahl1) / int(zahl2)
    print(str('Das Ergebnis ist ') + str(ergebnis))
    input('Drücke ENTER zum Beenden.')


if operation == str(1):
    plus()

if operation == str(2):
    minus()

if operation == str(3):
    mal()

if operation == str(4):
    geteilt()