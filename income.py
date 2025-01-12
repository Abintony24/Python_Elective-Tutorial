annual_income = float(input("Enter your income "))

tax = 0

if annual_income <= 300000:
  tax = 0
elif annual_income > 300000 and annual_income <= 700000:
  tax = (annual_income - 300000) * 0.05
elif annual_income > 700000 and annual_income <= 1000000:
  tax = 20000 + (annual_income - 700000) * 0.10
elif annual_income > 1000000 and annual_income <= 1200000:
  tax = 50000 + (annual_income - 1000000) * 0.15
elif annual_income > 1200000 and annual_income <= 1500000:
  tax = 80000 + (annual_income - 1200000) * 0.20
elif annual_income > 1500000:
  tax = 140000 + (annual_income - 1500000) * 0.30

print("Tax is ",tax)