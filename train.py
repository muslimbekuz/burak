''' MIT N-TASK '''


def palindromCheck(data):
    return data == data[::-1]


print(palindromCheck("level"))

''' MIT M-TASK


def getSquareNumbers(data):
    result = []
    for a in data:
        result.append({"number": a, "square": a**2})
    return result


print(getSquareNumbers([1, 2, 3]))
'''

''' MIT L-TASK


def reverseSentence(data):
    result = []
    for a in data.split():
        result.append(a[::-1])
    return " ".join(result)


print(reverseSentence("we like coding!"))
'''

''' MIT K-TASK 


def countVowels(data):
    count = 0
    for a in data:
        if a in "aeiou":
            count += 1
    return count


print(countVowels("tony"))
'''
