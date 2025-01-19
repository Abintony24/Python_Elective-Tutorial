input_str = input("Enter a string: ")
code = int(input("Enter the code: "))

print("Choose your option:")
print("1. Encrypt")
print("2. Decrypt")

option = int(input("Enter your option: "))

if option == 1:
    result_message = ""
    for char in input_str:
        if char.isalpha():
            if char.isupper():
                shift = ord(char) + code
                if shift > ord('Z'):
                    shift = shift - ord('Z') + ord('A') - 1
                result_message += chr(shift)
            elif char.islower():
                shift = ord(char) + code
                if shift > ord('z'):
                    shift = shift - ord('z') + ord('a') - 1
                result_message += chr(shift)
        else:
            result_message += char
    print("Encrypted Message:", result_message)

elif option == 2:
    result_message = ""
    for char in input_str:
        if char.isalpha():
            if char.isupper():
                shift = ord(char) - code
                if shift < ord('A'):
                    shift = ord('Z') - (ord('A') - shift - 1)
                result_message += chr(shift)
            elif char.islower():
                shift = ord(char) - code
                if shift < ord('a'):
                    shift = ord('z') - (ord('a') - shift - 1)
                result_message += chr(shift)
        else:
            result_message += char
    print("Decrypted Message:", result_message)

else:
    print("Invalid option!")
