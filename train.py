''' MIT Z-TASK'''


def sumEvens(array):
    sum = 0
    for n in array:
        if (n % 2 == 0):
            sum += n
    return sum


print(sumEvens([1, 2, 3]))

''' MIT Y-TASK


def findIntersection(array1, array2):
    result = []
    for n in array1:
        if n in array2:
            result.append(n)
    print(result)


findIntersection([1, 2, 3], [3, 2, 0])
'''

''' MIT X-TASK


def countOccurrences(obj, key):
    count = 0
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                count += 1
            count += countOccurrences(v, key)
    elif isinstance(obj, list):
        for item in obj:
            count += countOccurrences(item, key)
    return count


print(countOccurrences({"model": "A", "s": {"model": "B"}}, "model"))
'''

''' MIT W-TASK




def chunkArray(arr, chunk):
    result_arr = []

    for b in range(0, len(arr), chunk):
        temp_arr = []
        for a in range(chunk):
            if (b+a < len(arr)):
                temp_arr.append(arr[b+a])
        result_arr.append(temp_arr)
    return result_arr


print(chunkArray([1, 2, 3, 4, 5], 2))
'''

''' MIT V-TASK


def countChars(data):
    obj = {}
    for key in data:
        if (key in obj):
            obj[key] += 1
        else:
            obj[key] = 1
    return obj


print(countChars("muslim"))
'''

''' MIT T-TASK


def mergeSortedArrays(array1, array2):
    for a in array1:
        array2.append(a)
    return sorted(array2)


print(mergeSortedArrays([3, 1, 4], [2, 5]))
'''


''' MIT S-TASK


def missingNumber(numbers):
    n = len(numbers)
    return n * (n + 1) // 2 - sum(numbers)


print(missingNumber([0, 1, 2, 3, 4, 5, 6, 8, 9]))
'''


''' MIT R-TASK


def calculate(data):
    total = 0
    numbers = data.split("+")
    for a in numbers:
        total += int(a)
    return total


print(calculate("4 + 3"))
'''

''' MIT Q-TASK


def hasProperty(obj, str):
    return True if str in obj else False


print(hasProperty({"name": "PORSCHE 911"}, "name"))
'''

''' MIT P-TASK


def objectToArray(data):
    return [[key, value] for key, value in data.items()]


print(objectToArray({"a": 10, "b": 20}))
'''


''' MIT O-TASK


def calculateSumOfNumbers(data):
    sum = 0
    for i in data:
        if isinstance(i, int) and not isinstance(i, bool):
            sum += i
    return sum


print(calculateSumOfNumbers([50, "10", {"son": 10}, False, 50, True]))
'''


''' MIT N-TASK 


def palindromCheck(data):
    return data == data[::-1]


print(palindromCheck("level"))
'''

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
