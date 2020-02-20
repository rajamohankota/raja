#Program to accept the strings containing only vowels
def str_vowels(n):
    str1 = "aeiou"
    for i in n:
        if i in str1:
            pass
        else:
            return "Not accepted"
            break
        return "accepted"

n = input("Enter the string containing only vowels")
print(str_vowels(n))

