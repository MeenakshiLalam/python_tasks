count=0
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
      return x / y
    except ZeroDivisionError:
      print("we can't do division by zero")

print("list of operations")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
def validation():
    try:
        num1_value=int(num1)
        num2_value = int(num2)
        if num1_value>=0 and num2_value>=0:
             print(num1_value, "+", num2_value, "=", add(num1_value, num2_value))
             print(num1_value, "-", num2_value, "=", subtract(num1_value, num2_value))
             print(num1_value, "*", num2_value, "=", multiply(num1_value, num2_value))
             print(num1_value, "/", num2_value, "=", divide(num1_value, num2_value))
        elif num1_value<=0 and num2_value<=0:
            print(num1_value, "+", num2_value, "=", add(num1_value, num2_value))
            print(num1_value, "-", num2_value, "=", subtract(num1_value, num2_value))
            print(num1_value, "*", num2_value, "=", multiply(num1_value, num2_value))
            print(num1_value, "/", num2_value, "=", divide(num1_value, num2_value))


    except ValueError:
          print("invalid number")

next_calculation="yes"
while next_calculation=="yes":

        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        validation()
        count=count+1
        next_calculation = input("If you want to do next calculation? (yes/no): ")
        if next_calculation != "yes":
            break

print(f"{count} calculations users did: ")