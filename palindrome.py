# To check whether the string is a palindrome
def check_pali(test_string):
    if test_string == test_string[::-1]:
        print(True)
    else:
        print(False)

#Function call
if __name__ == "__main__":
    check_pali(test_string = input("Enter a test string: "))

