# Write a function called anagram that accepts gtwo striings and return True if they are anagrams and False
# if they aren't. anagram('listen', 'silent') should return True. anagram('cat', 'axe') should return False. 

def anagram(strOne, strTwo):
    #if lengths aren't same, not anagrams
    if len(strOne) != len(strTwo):
        return False

    #get counts for characters in each string
    strCountOne = {}
    strCountTwo = {}

    #since strings arae same length, doesn't matter which str I use here
    for letter in strOne:
        if letter not in strCountOne:
            strCountOne[letter] = 1
        else:
            strCountOne[letter] += 1

    for letter in strTwo:
        if letter not in strCountTwo:
            strCountTwo[letter] = 1
        else:
            strCountTwo[letter] += 1


        # check if value at key in one dictionary is equal to value in second dictionary (are the character counts the same? if not return false) 
    for key in strCountOne.keys():
        try:
            if strCountOne[key] != strCountTwo[key]:
                return False
        except KeyError:
            return False

    return True 

print(anagram('listen', 'silent'))
print(anagram('cat', 'axe'))