print("\n--- PITFALL 1: The Mutable Default Argument Trap ---")
def sammle(element, liste=[]):
    liste.append(element)
    return liste

print("Erster Anruf:", sammle("Akmed"))
print("Zweiter Aufruf", sammle("Bangura"))


