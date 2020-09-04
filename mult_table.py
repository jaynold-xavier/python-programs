size = input("Enter size of multiplication table : ")

print "     ",

for col_head in range(1,size+1) :
    print "{0:6}".format(col_head),

print "\n    +",

for lines in range(1,size+1) :
    print "------",

for row_head in range(1,size+1) :
    print "\n{0:3} |".format(row_head),
    for rows in range(1,size+1) :
        print "{0:6}".format(row_head*rows),
    print