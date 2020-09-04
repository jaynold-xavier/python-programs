n1 = raw_input("Enter a number to get number of digits: ")    #raw_input() accepts string
cnt = 0

while int(n1) > 0 :
    n1 = int(n1) // 10
    cnt += 1

print cnt