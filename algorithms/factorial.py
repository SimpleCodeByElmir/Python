
def factorial(number):
    result = 1;
    number = int(number)
    for i in range(2,number+1):
      result *= i
    return result


number = input(f"Please input a number to calculate factorial: ")
print(factorial(number))
