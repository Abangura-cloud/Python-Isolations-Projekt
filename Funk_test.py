print("\n--- PITFALL 1: The Mutable Default Argument Trap ---")
def sammle(element, liste=[]):
    liste.append(element)
    return liste

print("Erster Anruf:", sammle("Akmed"))
print("Zweiter Aufruf", sammle("Bangura"))

def mittelwert(zahlen):
    summe = 0
    anzahl = 0
    for zahl in zahlen:
        summe += zahl
        anzahl += 1
    ergebnis = summe / anzahl
    return ergebnis
# ------test the new function ----------
meine_zahlen = [10, 20, 30, 40]
schnitt = mittelwert(meine_zahlen)
print("Der Mittelwert ist:", schnitt)  # This will print 25.0
    
