def begruessung(name, anrede="Hallo"):
    text = f"{anrede}, {name}!"
    return text
print("Erster Aufruf:", begruessung("Akmed"))

def begruessung2(anrede="Hallo", vornme="Akmed", name="Bangura"):
    text2 = f"{anrede}, {vornme}, {name}!"
    return text2
print("Erster Aufruf:", begruessung2())
