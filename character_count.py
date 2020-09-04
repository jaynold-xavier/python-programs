data = raw_input("Enter a string and count the occurances of each character :")
length_data = range(len(data))

for a in length_data:
    count = 1
    for b in range(a+1,len(data)):
        if data[a] == data[b]:
            count += 1
            length_data.remove(b)
    print "Number of", data[a], ":", count


