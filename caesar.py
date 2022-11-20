'''
------------------------------------------------------------------------------------------------------------
Aufgabe 1
(a) Entschlüssele die in der Abbildung gezeigte Antwort von Asterix.

a=  KDOOR FDHVDU ZLU KDEHQ GHLQ YHUVFKOXHVVHOXQJVYHUIDKUHQ JHNQDFNW
->  HALLO CAESAR WIR HABEN DEIN VERSCHLUESSELUNGSVERFAHREN GEKNACKT

(b) Entschlüssele die Nachricht: Surjudpplhuxqj lvw hlqidfk qxu phjd jxw.

b= Surjudpplhuxqj lvw hlqidfk qxu phjd jxw
-> Programmierung ist einfach nur mega gut

(c) Verschlüssele analog eine selbst gewählte Nachricht. Benutze jetzt eine
Alphabetverschiebung um 7 Zeichen, die 'A' durch 'H' ersetzt ('B' durch 'I', 'C' durch 'I'). Gib
die Nachricht zusammen mit dem Schlüssel an deine Nachbarin bzw. deinen Nachbarn
weiter. Sie bzw. er soll die verschlüsselte Nachricht dann wieder entschlüsseln.

c= Immer wieder kommt es beim programmieren zu bis zu 1-2 Rechtschreibfehler.
-> Pttly dplkly rvtta lz ilpt wyvnyhttplylu gb ipz gb 8-9 Yljoazjoylpimlosly.

Aufgabe 2
(a) Das Python-Programm zur Buchstabenverschiebung funktioniert nicht, wenn man z.B.
zeichen = 'T' und schluessel = 10 vorgibt. Teste und begründe.

a= Wenn zu dem Acii Zeichen T = 84  einen schluessel von 10 hinzuzieht dann liegt das Ergebnis bie 94 = ^
Das Ergebis liegt nicht mehr in dem Bereich von A bis Z.


(b) Ändere das Python-Programm zur Buchstabenverschiebung so ab, dass es für alle
sinnvollen Vorgaben zeichen = ... und schluessel = ... korrekt funktioniert.

b= siehe mein Pytho Programm


Aufgabe 3
Der letzte Funktionsaufruf liefert noch nicht das beabsichtigte Ergebnis. Ändere die
Funktionsdefinition geeignet ab. Teste die Funktion dann mit weiteren Funktionsaufrufen.

->= siehe mein Pytho Programm


Aufgabe 4
Ergänze die Funktionsdefinitionen im folgenden Programmgerüst passend. Benutze für die
Funktion verschiebung das (korrekte) Ergebnis aus Aufgabe 3. Die Funktionsdefinition
zur Funktion verschluesselung kann sich am gezeigten Algorithmus orientieren. Günstig
ist es, die Funktion verschiebung dabei zu benutzen. Teste mit verschiedenen
Funktionsaufrufen.

->= siehe mein Pytho Programm

Aufgabe 5
(a) Texte, die mit der Funktion verschluesselung verschlüsselt wurden, können mit
derselben Funktion entschlüsselt werden, wenn man den Schlüssel geeignet wählt. Zeige
das mit geeigneten Beispielen.

->= siehe mein Pytho Programm

(b) Die Entschlüsselung von Texten, die mit dem Verschiebeverfahren verschlüsselt wurden,
sollen mit demselben Schlüssel entschlüsselt werden. Entwickle hierfür eine geeignete
Funktion entschluesselung

->= brauche ich nicht, weil bei mir der Schlüssel negativ angegeben werden kann
siehe mein Pytho Programm.

------------------------------------------------------------------------------------------------------------
'''
# Programmstartfunktionen
import random
import os

# Funkion Zeichenverschiebung mit fehlerausgleich
# Es werden nur Buchstaben und Zahlen beachtet.
# Alle anderen Zeichen werden so wie übergeben wieder zurück gegeben.
#
def f_verschiebung(f_zeichen, f_schluessel):
    f_zahl = ord(f_zeichen)
    if f_zahl>=48 and f_zahl<=57:
        if f_zahl+f_schluessel>57:
            f_neueZahl = f_zahl + f_schluessel - 10
        elif f_zahl+f_schluessel<48:    
            f_neueZahl = f_zahl + f_schluessel + 10
        else:   
            f_neueZahl = f_zahl + f_schluessel
    
    elif f_zahl>=97 and f_zahl<=122:
        if f_zahl+f_schluessel>122:
            f_neueZahl = f_zahl + f_schluessel - 26
        elif f_zahl+f_schluessel<97:    
            f_neueZahl = f_zahl + f_schluessel + 26
        else:
            f_neueZahl = f_zahl + f_schluessel
    
    elif f_zahl>=65 and f_zahl<=90:
        if f_zahl+f_schluessel>90:
            f_neueZahl = f_zahl + f_schluessel - 26
        elif f_zahl+f_schluessel<65:    
            f_neueZahl = f_zahl + f_schluessel + 26
        else:
            f_neueZahl = f_zahl + f_schluessel

   
    else:
        f_neueZahl = f_zahl

    f_neuesZeichen = chr(f_neueZahl)
    return f_neuesZeichen

# Sprungroutine für die Verschlüsselung jedes einzelnen Zeichens
#
def f_verschluesseln(f_wort, f_schluessel):
    f_ausgabe = ""
    for buchstabe in f_wort:
        f_buchstabe = f_verschiebung(buchstabe, f_schluessel)
        f_ausgabe = f_ausgabe + f_buchstabe
    return f_ausgabe


# Hauptprogramm
#
vorgabe1="VDOYH"
vorgabe2="DVWHULA"
vorgabe3="KDOORFDHVDUZLUK"
vorgabe4="GHLQYHUVFKOXHVVHOQJ"
vorgabe5="VYHUIDKUHQJHNQDFNW"
vorgabe6="Surjudpplhuxqj lvw hlqidfk qxu phjd jxw"

os.system('cls')

while True:
    print(f"""
    ---------------------------------------------------------------------
    Menu: 
    - (0) Ende des Programmes
    - (1) Vorgabe 1 nehmen = {vorgabe1}
    - (2) Vorgabe 2 nehmen = {vorgabe2}
    - (3) Vorgabe 3 nehmen = {vorgabe3}
    - (4) Vorgabe 4 nehmen = {vorgabe4}
    - (5) Vorgabe 5 nehmen = {vorgabe5}
    - (6) Vorgabe 6 nehmen = {vorgabe6}
    ---------------------------------------------------------------------
    Wenn Du eine Vorgabe auswählst oder ein verschlüsseltes Wort eingibt,
    gibt am besten den Schlüssel -1 ein und wähle 26 Durchläufe.
    In der Bildschirmausgabe siehst Du dann die Ergebnisse je Durchlauf.
    ---------------------------------------------------------------------
    """)
    _eingabe    =     input("Das zu verschlüsselnde Wort oder die Vorgabe wählen/eingeben: ")

    if _eingabe == "0":
        break
    else:
        if _eingabe == "1":
            _eingabe = vorgabe1
        elif _eingabe == "2":
            _eingabe = vorgabe2
        elif _eingabe == "3":
            _eingabe = vorgabe3
        elif _eingabe == "4":
            _eingabe = vorgabe4
        elif _eingabe == "5":
            _eingabe = vorgabe5
        elif _eingabe == "6":
            _eingabe = vorgabe6

    print(f"                                  Deine Eingabe/Vorgabe ist : {_eingabe}")
    _schluessel = int(input("Bitte gebe den Schlüssel an                                 : "))
    _durchlauf  = int(input("Bitte gebe die Durchläufe der Verschlüsselungen an          : "))
    _lauf=1
    while  _lauf<=_durchlauf:
        a_eingabe = list(_eingabe)
        _ergebnis=f_verschluesseln(a_eingabe,_schluessel)
        print(f"Durchlauf ( {_lauf} ) = {_ergebnis}")
        _eingabe = _ergebnis
        _lauf=_lauf+1

print("Ende")
