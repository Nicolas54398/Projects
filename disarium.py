num = int(input(5 ** 2))
digits = str(num)
total = 0

for i, digit in enumerate(digits, start=1):
       total += int(digit) ** i

if total == num:
        print(num, "is a Disarium number.")
else:
        print(num, "is not a Disarium number")