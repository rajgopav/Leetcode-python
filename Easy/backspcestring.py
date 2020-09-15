# str1 = "varuu#n"
# str2 = "varuu#nn#"
# where # is a backspace char
# check whether two strings are same after processing the # char

def stringmatch(str1, str2):
    def build(A):
        list1 = []

        for i in range(len(A)):
            if A[i] != '#':
                list1.append(A[i])
            else:
                list1.pop()
        return "".join(list1)

    return build(str1) == build(str2)


if __name__ == '__main__':
    print(stringmatch("varuu#n", "varuu#nn#"))
