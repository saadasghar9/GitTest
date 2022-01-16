# program for even  and odd number 

num = int(input("enter number"))

if (num % 2) == 0:
    print(num, "is a even number")
else:
    print(num,"is a odd number")

#code explaination

# program for prime numbers
# goes here

# program for tables
table = int(input("enter number"))

for i in range(1,11):
    j = table * i
    print(table," *",i,"=",j)
    
    