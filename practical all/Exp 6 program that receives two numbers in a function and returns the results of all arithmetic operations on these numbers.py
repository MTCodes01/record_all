#program that receives two numbers in a function and returns the results of all arithmetic operations(+,-,*,/,%) on these numbers
def arCal(x,y):
    return x+y,x-y,x*y,x/y,x%y
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
add,sub,mult,div,mod=arCal(num1,num2)
print("Sum of the given numbers:",add)
print("Subtraction of the given numbers:",sub)
print("Product of the given numbers:",mult)
print("Division of the given numbers:",div)
print("Modulo of the given numbers:",mod)