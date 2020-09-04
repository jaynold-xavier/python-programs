# program to play minion game

if __name__ == "__main__":
    s= raw_input("Enter a word: ")

    def get_vowels(characters):
        temp = []
        for item in characters:
            if item in ['a','e','i','o','u']:
                temp.append(item)
        return temp

    def get_consonants(characters):
        temp = []
        for item in characters:
            if item not in ['a','e','i','o','u']:
                temp.append(item)
        return temp

    def form_subwords(name,letters_list):
        temp = []
        for i in range(len(s)):
            if s[i] in letters_list:
                for m in range(i, len(s)):
                    if s[i:m + 1] not in temp:
                        print s[i:m + 1]
                    temp.append(s[i:m + 1])

        print "\n", name, len(temp), "\n"

    form_subwords("Stuart",get_vowels(s))
    form_subwords("Kevin",get_consonants(s))

