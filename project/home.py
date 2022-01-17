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

# basic math

num1 = 2
num3 = 7

#addition

addtotal = num1 + num3

print(num1,"+",num3,"=",addtotal)

# subtraction 

subtotal = num1 - num3
print(num1,"-",num3,"=",subtotal)