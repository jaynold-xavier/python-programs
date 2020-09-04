num = input("Enter a num: ")
orig = num
large2 = num%10
num = num / 10

while num > 0:
   if large2 < num%10:
       large2 = num%10
   num /= 10

while orig > 0:
   if large2 < orig%10:
       large2 = orig%10
   orig /= 10

print large2