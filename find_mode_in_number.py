#Find mode of a number
if __name__ == "__main__":
    num = input("Enter a number: ")
    cmp1 = 1
    cmp2 = 1
    mode = 0

    while (num>0):
        a,temp = num%10,num/10
        cmp1 = 1

        while(temp>0):
            if a == (temp%10):
                cmp1+=1
            temp/=10

        if cmp1 > cmp2: mode = a
        cmp2 = cmp1
        num/=10

    print "Mode=",mode