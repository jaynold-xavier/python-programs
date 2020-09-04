#to print rangoli with alphabets

alphabets = "abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    size = input("Enter size: ")

    def alpha_rang(a,b,c):
        for i in range(a,b,c):
            for t in range(i * 2):
                print "-",
            for m1 in range(size - 1, i, -1):
                print alphabets[m1],
                print "-",
            for m2 in range(i, size, 1):
                print alphabets[m2],
                if m2 + 1 != size: print "-",
            for b in range(i * 2):
                print "-",
            print

    alpha_rang(size - 1,-1,-1)
    alpha_rang(1,size,1)
