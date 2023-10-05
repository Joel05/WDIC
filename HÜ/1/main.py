list = []
while True:
    inputstring=input("Ganzahl eingeben: ")
    if inputstring == "":
        break
    else:
        try:
            list.append(int(inputstring))
        except ValueError:
            print("Ganze Zahlen bitte!")


print(f"Maximum: {max(list)} Minimum: {min(list)} Durchschnitt: {sum(list)/len(list)} Summe: {sum(list)}")