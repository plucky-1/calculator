# Asimple calculator App

print("""*******
1.Addition
2.Subtraction
3.Multiplication
4.Division
  Exponential
************""") 

print("Enter two numbers  Add")
#promt the user for a number and store it
firstNumber = input("first number:")
#prompt user for a second number and store it
secondNumber = input("secondNumber:")
sum = float(firstNumber) +  float(secondNumber)
print(f"{firstNumber} + {secondNumber} = {sum :.2f}")

print("***********")
print("Subtraction")
print("Enter two numbers to subtract")
#promt the user for a number and store it
firstNumber = input("first number:")
#prompt user for a second number and store it
secondNumber = input("secondNumber:")
sub = float(firstNumber) -  float(secondNumber)
print(f"{firstNumber} - {secondNumber} = {sub :.2f}")

print("Divission")
print("Enter two numbers to Divid")
#promt the user for a number and store it
firstNumber = input("first number:")
#prompt user for a second number and store it
secondNumber = input("secondNumber:")
div = float(firstNumber) /  float(secondNumber)
print(f"{firstNumber} / {secondNumber} = {div :.2f}")

print("Exponetial")
print("Enter two numbers for Exponential")
#promt the user for a number and store it
firstNumber = input("first number:")
#prompt user for a second number and store it
secondNumber = input("secondNumber:")
expo = float(firstNumber) **  float(secondNumber)
print(f"{firstNumber} ** {secondNumber} = {expo :.2f}")

print("Floordivision")
print("Enter two numbers to perform floordivition")
#promt the user for a number and store it
firstNumber = input("first number:")
#prompt user for a second number and store it
secondNumber = input("secondNumber:")
floordiv = float(firstNumber) //  float(secondNumber)
print(f"{firstNumber} // {secondNumber} = {floordiv :.2f}")

