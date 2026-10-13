namen = ["Anna", "Ben", "Clara", "David", "Elif"]

if len(namen) == 0:
    print("Liste ist leer")
elif len(namen) == 1:
    print("Genau ein Name")
else:
    print("Mehrere Namen vorhanden")

for name in namen:
    print(name)

for index, name in enumerate(namen):
    print(index, name)

for i in range(5):
    print(i)

rest = 10
while rest >0:
    rest-=3
    print(rest)

for name in namen:
    if name == "Clara":
        continue
    if name == "David":
        break
    print(name)

wert = (0, 0)
if wert == (0, 0):
    print("Ursprung")
elif isinstance(wert, tuple) and len(wert) == 2 and wert[0] == 0:
    print("Auf der y-Achse")
elif isinstance(wert, tuple) and len(wert) == 2:
    print("Punkt in der Ebene")
else:
    print("Unbekannte Form")

match wert:
    case(0, 0):
        print("Ursprung")
    case(0, y):
        print("Auf der y-Achse")
    case(x, y):
        print("Punkt in der Ebene")
    case _:
        print("Unbekannte Form")

match wert:
    case (x, y) if x == y:
        print("Auf der Winkelhalbierenden")
    case (x, y):
        print("Punkt in der Ebene")

tag = "So"
match tag:
    case "Sa" | "So":
        print("Wochenende")
    case _:
        print("Werktag")


        
        
    