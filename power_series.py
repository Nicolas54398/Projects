# Power Series Maker In Python!
#It prints 1 + x + x^2 + x^3 + ... up to n terms

#Input from user
x = int(input("Enter the value of x:"))
n= int(input("Enter the number of terms:"))

print ("/nPower Series:")

# Looping Through Terms
for i in range(n):
    term = x** i
    print(f"Term {i + 1}: {x}^{i} = {term}")