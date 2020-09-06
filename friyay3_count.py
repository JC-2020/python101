# Write a function called count that accepts a string and returns a dictionary containing the counts of each character in the string.
# count('abccc') should return {"a": 1, "b" : 1, "c" : 3} 

def count(str):
    countDic = {}
    for character in str:
        if countDic.get(character, False):
            countDic[character] += 1
        else:
            countDic[character] = 1
    return countDic

print(count("abccc"))