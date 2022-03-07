
# Define variables
fizz = 3
buzz = 5

# Loop in range 1 to 100
for number in range (1,100):
    # Multiples of both variables
    if number % (buzz * fizz) == 0:
        print ("FizzBuzz")
    # Multiples of number 3
    elif number % fizz == 0:
        print ("Fizz")
    # Multiples of number 5
    elif number % buzz == 0:
        print ("Buzz")
    # Different number
    else:
        print (number)