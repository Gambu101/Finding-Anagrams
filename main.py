# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(firstWord = "", secondWord = ""):
    # [assignment] Add your code here
    firstWord = input("Enter a word: ")
    secondWord = input("Enter a word: ")
    firstWord.replace(" ","")
    secondWord.replace(" ","")
    firstWord = firstWord.lower()
    secondWord = secondWord.lower()

    if sorted(firstWord)==sorted(secondWord):
        return True
    return False

print(find_anagram())
