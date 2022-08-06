# To check if a string is a valid shuffle of two other strings
def valid_shuffle(string1, string2, string3):
    string4 = string1 + string2
    list1 = []
    list2 = []
    for i in string4:
        list1.append(i)
    for i in string3:
        list2.append(i)
    for i in list1:
        for j in list2:
            if i == j:
                list2.remove(j)
    if list2 == []:
        print(True)
    else:
        print(False)

# Function call
if __name__ == '__main__':
    valid_shuffle("XY", "12", "Y1X2")



