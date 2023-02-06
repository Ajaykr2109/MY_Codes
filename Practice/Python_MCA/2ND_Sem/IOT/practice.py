def findCaps(n):
    numOfCaps = 0
    numOfLower = 0
    # normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(n)):
        if n[i].isupper():
            numOfCaps += 1
        if n[i].islower():
            numOfLower += 1
    print("\nNumber Of Caps in", "[", n, "]", " is", numOfCaps)
    print("Number Of Lower in", "[", n, "]", " is", numOfLower, "\n")


def stringPalindrome(n):
    if n == n[::-1]:
        print("[", n, "]", "is Palindrome\n")
    else:
        print("Not Palindrome\n")


def stringPangram(n):
    normal = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(normal)):
        if normal[i] not in n:
            print("Not Pangram\n")
            return
    print("[", n, "]", "\nGiven sentence is Pangram.\n")


findCaps("Hello WorlD")
stringPalindrome("madam")
stringPangram("ajay")
