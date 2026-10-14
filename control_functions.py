# ==========================================================
# PART 1: Control Flow & Match Statements (List Patterns)
# ==========================================================

# Test data: Change this list to test different conditions!
# Try changing it to: ["show"] or ["help", "me", "now"]
befehl = ["delete", "hallo.txt"]

match befehl:
    case [aktion]:
        print(f"Einfache Aktion erkannt: Ich werde {aktion} ausführen.")
        
    case ["delete", dateiname]:
        print(f"⚠️ ACHTUNG: Die Datei '{dateiname}' wird jetzt gelöscht!")
        
    case ["help" | "hilfe", *_]:
        print("Hilfemenü: Du kannst 'show' oder 'delete [dateiname]' eingeben.")
        
    case _:
        print("Fehler: Unbekanntes Befehlsformat.")

# ==========================================================
# PART 2: Functions and Their Two Pitfalls
# ==========================================================

print("\n--- PITFALL 1: The Mutable Default Argument Trap ---")
def name_hinzufuegen(neuer_name, namen_liste=[]):
    namen_liste.append(neuer_name)
    return namen_liste

print("Erster Aufruf:", name_hinzufuegen("Ali"))
print("Zweiter Aufruf:", name_hinzufuegen("Ben"))  # Wait, why is Ali still here?!


print("\n--- PITFALL 2: The Scope Shadowing Trap ---")
anzahl = 10  # Global variable

def berechne():
    anzahl = 5  # This creates a local 'anzahl', hiding the global one!
    print("Innerhalb der Funktion (lokal):", anzahl)

berechne()
print("Außerhalb der Funktion (global):", anzahl)  # It stayed 10!
