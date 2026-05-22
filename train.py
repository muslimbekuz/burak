''' MIT L-TASK'''


def reverseSentence(data):
    result = []
    for a in data.split():
        result.append(a[::-1])
    return " ".join(result)


print(reverseSentence("we like coding!"))

''' MIT K-TASK 


def countVowels(data):
    count = 0
    for a in data:
        if a in "aeiou":
            count += 1
    return count


print(countVowels("tony"))
'''
