word = input("Give a word")

def palindrome(word):
    return word == word[::-1]

check_palindrome = palindrome(word)

if check_palindrome:
    print("The word {} is a palindrome".format(word))
else:
    print("The word {} is NOT a palindrome".format(word))