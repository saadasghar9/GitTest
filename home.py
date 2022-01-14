# prime numbers 
### numbers that either multiply by 1 or by itself

number = 90

if number > 1:
    for i in range (2, number):
        if (number % i) == 0:
            print(number,"is not a prime number")
            break
        else:
            print(number,"is a prime number")
else:
    print(number,"invalid")    