
a = int(input("enter a num "))
if a <=1:
    print("not a prime number")
else :
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
         print("not prime")
         break
    else:
        print('is prime')  