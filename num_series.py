n = input("Enter a number to get its series: ")
total = 0

print 0,

for i in range(1,n+1):
    total+=i
    print "+ %d" %(i),

print "= %d" %(total)
