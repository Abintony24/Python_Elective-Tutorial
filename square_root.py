num = int(input("Enter a number: "))
if num <= 0:
    print("Invalid input")
    exit(0)

x = num
while True:
    root = 0.5 * (x + num / x)
    if abs(root - x) < 0.0001:
        break
    x = root

print(f'{root:.4f}')
