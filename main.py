import random
import time

benutzerKontoStand = 0 # in Coins
spielKontoStand = 0 # in Coins

benutzerKontoStand += 100 # 100 Coins Startguthaben

einleitung = "Willkommen zum Glückspiel! \n\
    Alles - oder - nichts. \n\
    Sie entscheiden."

hilfsText = "\
    Benutzen sie folgende Befehle, um mit dem Spiel zu interagieren! \n\
    \n \
    H - Geben sie diesen Hilfstext aus \n \
    I - Info über deinen Kontostand und das Spielfeld \n \
    E - Coins einzahlen \n \
    A - Coins auszahlen \n \
    G - Verdopple deine Coins oder verliere es. Lass' das Glück spielen! \n \
    B - Beende das Spiel"

spielLäuft = True


print(einleitung)

while (benutzerKontoStand > 0 or spielKontoStand > 0) and spielLäuft:
    eingabe = input("Eingabe (H für Hilfe): ")

    if eingabe == "H":
        print(hilfsText)
    elif eingabe == "I":
        print("Auf dem Spielfeld liegen", spielKontoStand, "💵")
        print("Auf deinem Konto sind", benutzerKontoStand, "💵")
    elif eingabe == "E":
        zahlung = input("Wie viele 💵 möchtest du einzahlen?: ")
        zahlung = min(benutzerKontoStand, int(zahlung))
        spielKontoStand += zahlung
        benutzerKontoStand -= zahlung
        print("Du hast", zahlung, "💵 eingezahlt und nun", spielKontoStand, "💵 auf dem Spielstand.")
    elif eingabe == "A":
        print("Alle", spielKontoStand, "💵 auf dem Spielfeld an dein Konto ausgezahlt")
        benutzerKontoStand += spielKontoStand
        spielKontoStand = 0
        print("Auf deinem Konto sind jetzt", benutzerKontoStand, "💵")
    elif eingabe == "G":
        print("Lasset das Glück spielen!")
        for i in range(0,5):
            time.sleep(1)
            print(".")
        time.sleep(2)
        print()
        if random.randint(1,100) >= 50:
            print(spielKontoStand, "💵 auf dem Spielfeld auf", spielKontoStand * 2, "💵 verdoppelt!")
            spielKontoStand *= 2
        else:
            print(spielKontoStand, "💵 auf dem Spielfeld auf 0 💵 zurückgesetzt.")
            spielKontoStand = 0
    elif eingabe == "B":
        spielLäuft = False
    else:
        print("Ungültige Eingabe. Um die möglichen Befehle aufzulisten, gib 'H' ein.")
    print("")
        

print("Spiel beendet.")

if spielKontoStand > 0:
    print("Restliche", spielKontoStand, "💵 auf dem Spielfeld an dich ausgezahlt.")
    benutzerKontoStand += spielKontoStand
    spielKontoStand = 0

print("Dein End-Kontostand:", benutzerKontoStand, "💵")