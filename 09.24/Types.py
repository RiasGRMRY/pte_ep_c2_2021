input_data = input("Kérek egy egész szémot: ")
try:

    int_number = int(input_data)
    print("A szám 3-szorosa: ", 3 * int_number)
    print(type(input_data))
    print(type(int_number))

except ValueError:
    print("Nem egész számot adott meg!")


input_data = input("Kérek egy valós számot: ")
try:

    float_number = float(input_data)
    print("A szám 3-szorosa: ", 3 * float_number)
    print(type(input_data))
    print(type(float_number))

except ValueError:
    print("Nem valós számot adott meg!")