# =====================================================================
# Task 1: The Mutable Default Argument Pitfall
# =====================================================================

def notiere(eintrag, protokoll=[]):
    protokoll.append(eintrag)
    return protokoll

# --- Triggering the pitfall ---
print("--- Task 1: Triggering Mutable Default Argument ---")
# Call it three times and print the result each time
print(notiere("First Entry"))
print(notiere("Second Entry"))
print(notiere("Third Entry"))


def notiere_korrigiert(eintrag, protokoll=None):
    # Fix: To ensure a fresh list is created if no argument is passed
    if protokoll is None:
        protokoll = []
    protokoll.append(eintrag)
    return protokoll

# --- Verifying the fix ---
print("\n--- Task 1: Fixed Version ---")
# Call it three times and verify each starts with a fresh list
print(notiere_korrigiert("First Entry"))
print(notiere_korrigiert("Second Entry"))
print(notiere_korrigiert("Third Entry"))


# =====================================================================
# Task 2: The Missing return Pitfall
# =====================================================================

def mittelwert_fehlerhaft(zahlen):
    if not zahlen:
        return 0
    ergebnis = sum(zahlen) / len(zahlen)
    # Intentionally missing the return statement

# --- Triggering the pitfall ---
print("\n--- Task 2: Triggering Missing Return ---")
meine_zahlen = [10, 20, 30, 40, 50]
resultat_alt = mittelwert_fehlerhaft(meine_zahlen)
print(f"Value: {resultat_alt}")
print(f"Type: {type(resultat_alt)}")


def mittelwert(zahlen):
    if not zahlen:
        return 0
    ergebnis = sum(zahlen) / len(zahlen)
    return ergebnis  # Fix: Added missing return statement

# --- Verifying the fix ---
print("\n--- Task 2: Fixed Version ---")
resultat_neu = mittelwert(meine_zahlen)
print(f"Value: {resultat_neu}")
print(f"Type: {type(resultat_neu)}")
