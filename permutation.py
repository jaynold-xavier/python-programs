text = raw_input("Enter a string: ")
temp = range(0,len(text)+1)

for a in range(0,len(text)) :
    for b in range(0, len(text)):
        if a!=b:
            for c in range(0, len(text)):
               if(b!=c and a!=c):
                    print text[a] + text[b] + text[c]