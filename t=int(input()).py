t=int(input())

#write your code here


i = 0
while (i < t) :
    n = input()
    div = 2
    while (div * div <= n) :
        if (n % div == 0) :
            break
        div += 1
    if (div * div > n) :
        print("prime")                  
    else :
        print("not prime")
    i += 1