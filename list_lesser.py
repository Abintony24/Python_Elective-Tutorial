master = []  
while True:  
    char = input('Enter a number to add to the list (or type "n" to stop): ')  
    if char.lower() == 'n':  
        break  
    if char.isdigit():  
        master.append(int(char))  
    else:  
        print("Invalid input. Please enter a valid number.")  

number = int(input("Enter the number: "))  

new_list = [num for num in master if num < number]  
print(f"List with numbers smaller than {number} is {new_list}")