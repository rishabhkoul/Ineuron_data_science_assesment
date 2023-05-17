def valid_string(string):
    try:
        chars = string.lower()

        char = []
        freq = {}
        check = 0
        for i in chars:
            if i not in char:
                char.append(i)
        for i in char:
            freq[i] = chars.count(i)
        
        print(freq)

        for i in freq.values():
            if i != 1:
                check = 1
            else:
                check = 0  

        if check == 1:
            print("NO")
        elif check == 0 :
            print("YES")
    except Exception as e:
        pass

if __name__ == "__main__":
    valid_string("abc")
    valid_string("abcc")
    valid_string("abcdefghijkl")
    valid_string("12345abcd")
    valid_string("abc abc abc")
    valid_string("aBbb")
    