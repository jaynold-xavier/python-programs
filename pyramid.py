num = input("Enter num: ")

for i in range(1,num+1):
    for b in range(i,num):
        print " ",
    for j in range(1,i*2):
        print "*",
    print