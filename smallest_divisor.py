num = input("Enter a number to check for smallest divisor: ")
print "\nThe proper divisors of", num , "are:" ,

for i in range(2,num):
    if num % i == 0: print i,