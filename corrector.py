print("\n--- PITFALL 1: The Mutable Default Argument Trap ---")
def notiere(eintrag, protokoll=[]):
    protokoll.append(eintrag)
    return protokoll

# --- Three calls to trigger and observe the bug ---
print("--- Buggy Version (Shared List) ---")
print("Erster Aufruf:", notiere("Akmed"))
print("Zweiter Aufruf:", notiere("Bangura"))
print("Dritte Aufruf:", notiere("Cloud"))  # Watch it grow to 3 items!


print("\n--- PITFALL 2: The Mutable Default Argument Trap ---")
# 2. Mein korrigiert Version
def notiere_korrigiert(eintrag, protokoll=None):
    # Hier wird Korriert
    if protokoll is None:
        protokoll = []   # Creates a fresh list object inside local scope
    protokoll.append(eintrag)
    return protokoll
# --- Three calls to verify the independent behavior ---
print("\n--- Corrected Version (Fresh List Each Time) ---")
print("Erster Aufruf:", notiere_korrigiert("Akmed"))
print("Zweiter Aufruf:", notiere_korrigiert("Bangura"))
print("Dritte Aufruf:", notiere_korrigiert("Cloud"))  # Stays exactly 1 item!


print("\n--- PITFALL :----Berechne --------------------------------")
anzahl = 10  # Global variable
def berechne_korrigiert():
    global anzahl  # <-- This links to the global variable
    anzahl = 5     # This now changes the global variable permanently!
    print("Innerhalb:", anzahl)

berechne_korrigiert()
print("Außerhalb:", anzahl)  # This will now print 5!

print("\n--- PITFALL :--------Mittelwert------------------------")
def mittelwert(zahlen):
    # If the list is empty, return 0 to prevent a ZeroDivisionError
    if not zahlen:
        return 0
      
    gesamtsumme = 0
    for zahl in zahlen:
        gesamtsumme += zahl
        
    # Divide the total sum by the count of numbers
    ergebnis = gesamtsumme / len(zahlen)
    return ergebnis

# ------test the new function ----------
meine_zahlen = [10, 20, 30, 40]
schnitt = mittelwert(meine_zahlen)
print("Der Mittelwert ist:", schnitt)  # This will print 25.0