# program split a word s into k (factor of len(s)) segments and remove duplicate letters
#           in each segment from behind(keep front original)

if __name__ == "__main__":
    s = "AABCABAADADA"     #raw_input("Enter a word: ")
    k = 3                #input("Enter length of each subsegment: ")

    words = []

    for i in range(len(s)/k):
        words.append(list(s[i*3:i*3+k]))
        print "".join(words[i]), "=",
        t, b = [], 0
        while b < len(words[i]):
            if words[i][b] in t:
                words[i].pop(b)
            else:
                t.append(words[i][b])
                b = b + 1
        print "".join(words[i])
