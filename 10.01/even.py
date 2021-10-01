is_number = False
while not is_number:

    try:
        number = int(input("Adjon meg egy integer számot: "))
        is_number = True

        if number % 2 == 0:
            print("A szám páros")
        else:
            print("A szám páratlan")

    except ValueError:
        print("Hiba!: ")