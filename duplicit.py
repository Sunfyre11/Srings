# To find duplicates in a string and print their count
def check_dup(string1, string2):
    list_count = []
    string3 = ""
    for i in string1:
        if i not in string3:
            string3 += i
    print(string3)
    for j in string3:
        count = 0
        for k in string2:
            if j == k:
                count += 1
        if count != 0:
            list_count.append("count[{a}] = {b}".format(a = j, b = count))
    final_list = []
    for element in list_count:
        if element not in final_list:
            final_list.append(element)
    for value in final_list:
        print(value)

# Function call
if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    check_dup(string1, string2)