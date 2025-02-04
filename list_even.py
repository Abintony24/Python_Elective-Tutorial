master = list(map(int, input("Enter list of numbers: ").split()))  
new_list = sorted([num for num in master if num % 2 == 0])  
print(new_list)