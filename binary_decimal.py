binary = input("Enter binary number:")
pw = 0
dec = 0

for char in binary[::-1]:
    if int(char) > 1:
        print("Invalid input")
        exit()

    dec += int(char) * 2 ** pw
    pw += 1

print("Decimal:", dec)
