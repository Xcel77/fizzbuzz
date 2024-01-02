# FizzBuzz Challenge - Jan 2, 2024
# create a loop to go through the numbers 1 - 100
# if the number is divisible by 3, print "Fizz"
# if the number is divisible by 5, print "Buzz"
# if the number is divisible by 3 and 5, print "FizzBuzz"

for i in range(1, 101):  # Loop Through 1 - 100
    if i % 3 == 0 and i % 5 == 0:  # Check if divisible by 3 and 5
        print("FizzBuzz")
    elif i % 5 == 0:  # Check if divisible by 5
        print("Buzz")
    elif i % 3 == 0:  # Check if divisible by 3
        print("Fizz")
    else:  # If not divisible by 3 or 5 just print the number
        print(i)
