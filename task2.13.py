# a = input("enter the word")
# if a == a[::-1]:
#    print('Палиндром')
# else:
#    print('False')


# def isPalindrome(myString):
#     return myString == myString[::-1]
word = input()
def isPalindrome(word):
    return word == word[::-1]
print(isPalindrome(word))
#word = input()
#def palindrome(word):
#    for i in range(len(word) // 2):
#        if word[i] != word[-1 - i]:
#            return False
#            return True
#print(palindrome(word))
#S = input("Input a word: ")


#def isPalindrome(S):
#    for i in range(0, len(S)):
#        if S[0 + i] == S[len(S) - 1]:
#            return "True"
#        else:
#            return "False"
#print(isPalindrome(S))
