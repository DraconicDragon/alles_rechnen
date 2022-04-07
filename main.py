#Primzahlen, vollkommene Zahlen und befreundete Zahlen berechnen
#jeweils unter Verwendung der selbst definierten Funktion t_summe(a)
# 1. Teil
def t_summe(zahl):
    teilers = 0
    i=1
    while i<=zahl // 2:
        if zahl % i == 0:
            teilers=teilers+i
        i=i+1
    return(teilers)
# 2.Teil
print("Das Programm sucht wahlweise Primzahlen, vollkommenen Zahlen oder befreundete Zahlen")
print("in einem vom Benutzer zu wählenden Bereich")
print("Der Benutzer kann einen Anfangs- und einen Endwert angeben. Falls kein Anfangswert")
print("angegeben wird, startet das Programm automatisch bei 1")
print()
print("Wenn Sie Primzahlen bestimmen wollen, geben Sie eine 1 ein!")
print("Für vollkommene Zahlen bitte eine 2")
print("Für befreundete Zahlen eine 3")
print("Für alles bitte eine 0")
print()
# 3. Teil
wahl=int(input())
u_gr = input('Geben Sie ein, ab welcher Zahl gesucht werden soll: ')
o_gr = int(input('Geben Sie ein, bis zu welcher Zahl gesucht werden soll: '))
if u_gr=="":
    zaehler=1
else:
    zaehler=int(u_gr)
    hilfszaehler=zaehler

# 4. Teil
if wahl==1 or wahl ==0:
    while zaehler<=o_gr:
        p_test=t_summe(zaehler)
        if p_test==1:
            print(zaehler," ist eine Primzahl")
        zaehler=zaehler+1
    zaehler=hilfszaehler

# 5. Teil
if wahl==2 or wahl==0:
    while zaehler<=o_gr:
        ts=t_summe(zaehler)
        if ts==zaehler:
            print(zaehler," ist eine vollkommene Zahl")
        zaehler=zaehler+1
    zaehler=hilfszaehler

# 6. Teil
if wahl==3 or wahl ==0:
    gefunden=False
    while zaehler<=o_gr:
        a = t_summe(zaehler)
        b =t_summe(a)
        if zaehler==b and zaehler!=a:
            print(zaehler,' und ',a,' sind befreundete Zahlen')
            gefunden=True
        zaehler=zaehler+1
    if gefunden == False:
        print ('Es gibt keine befreundeten Zahlen in diesem Bereich')


