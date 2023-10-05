width = int(input("Bitte geben Sie die Breite der Tabelle ein: "))
height = int(input("Bitte geben Sie die Höhe der Tabelle ein: "))



for i in range(height):
    if i == 0:
        for j in range(width):
            print("+---", end="")
        print("+")
    for j in range(width):
        if (i+j) % 2 == 0:
            print("| X ", end="")
        else:
            print("| O ", end="")
    print("|")
    for j in range(width):
        print("+---", end="")
    print("+")

