rows = input("Enter length of inverted star : ")

for i in range(0, rows) :

    for b in range(0,i) :
        print " ",

    for a in range(i,rows) :
        print "*",

    print "\n"