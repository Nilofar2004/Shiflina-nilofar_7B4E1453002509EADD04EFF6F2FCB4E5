#Implement a recursive function to calculate the factorial of a given number

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)


number = int(input("ENTER A VALUE:"))
fact = factorial(number)
print("THE FACTORIAL OF", number, "IS", fact)
