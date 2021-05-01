import Calculate

print("Please two number for calculate operator basic....")
print()
num = int(input("Enter num one please: "))
num2 = int(input("Enter num two please: "))
print()
print("Calculate the operator.................")
print()

calculate = Calculate.Calculate(num, num2)

print(f"Teh sun is : {calculate.sum()}")
print(f"The subtraction is: {calculate.subtraction()}")
print(f"The Divide is: {calculate.divide()}")
print(f"The Multiply is: {calculate.multiply()}")

print()
print("Calculate the operator finish.................")
print("Thanks....")
