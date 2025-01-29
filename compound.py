#copound interest

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("enter the principal amount: "))
    if principal <= 0:
        print("principal can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("enter the interest rate: "))
    if rate <= 0:
        print("interest rate can't be less than or equal to zero")
while time <= 0:
    time = float(input("enter the time: "))
    if time <= 0:
        print("time can't be less than or equal to zero")

total = principal * pow((1 + rate / 100), time)
print(f"balance after {time} year/s: ${total:.2f}")