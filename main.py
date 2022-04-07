# Funktionsdefinition
def teilersumme(zahl):
    ts_func = 0
    teiler = 1
    while teiler <= zahl / 2:

        if zahl % teiler == 0:
            ts_func = ts_func + teiler

        teiler += 1
    return ts_func

# Benutzeranweisung
print("Das Programm sucht Primzahlen, vollkommene Zahlen und/oder befreundete Zahlen nach Wahl\n")
print("Bitte geben Sie zur Auswahl eine Zahl ein: \n",
          "1 für Primzahlen\n",
          "2 für volkommende Zahlen\n",
          "3 für befreundete Zahlen\n",
          "0 für alle Zahlen\n")

# Zuweisung der Eingaben zu Variablen
auswahl = int(input("Ihre Wahl: "))
untere_gr = int(input("Welche Zahl soll die untere Grenze werden? "))
obere_gr = int(input("Welche Zahl soll die obere Grenze werden? "))

ausgabenzaehler = 0


# Primzahlenprüfer
if auswahl == 0 or auswahl == 1:
    ts = 0
    print("")

    while untere_gr <= obere_gr:
        if teilersumme(untere_gr) == 1:
            if untere_gr == 1: # 1 ist keine Primzahl
                print("")
            else:
                print(untere_gr, end = ", ")
                ausgabenzaehler += 1

        untere_gr += 1

    if ausgabenzaehler > 0:
        print("\nPrimzahlen im angegebenen Bereich wurden ausgegeben.")
    else:
        print("Keine Primzahlen im angegebenen Bereich gefunden. (1 ist keine Primzahl!)")

print("")

# vollkommene Zahlenprüfer
if auswahl == 0 or auswahl == 2:

    while untere_gr <= obere_gr:
        ts = teilersumme(untere_gr)

        if ts == untere_gr:
            print(untere_gr, end = ", ")
            ausgabenzaehler += 1

        untere_gr += 1

    if ausgabenzaehler > 0:
        print("\nVollkommene zahlen wurden ausgegeben.")
    else:
        print("Keine vollkommenen Zahlen im Bereich gefunden.")

print("")

# Befreundete Zahlenprüfer
if auswahl == 0 or auswahl == 3:

    while untere_gr <= obere_gr:
        a = teilersumme(untere_gr)
        b = teilersumme(a)

        if untere_gr == b and untere_gr != a:
            print(untere_gr, "und", a, end = ",\n")
            ausgabenzaehler += 1

        untere_gr += 1

    if ausgabenzaehler > 0:
        print("\nBefreundete zahlen wurden ausgegeben.")
    else:
        print("Keine befreundete Zahlen im Bereich gefunden.")
