def binary_search(arr, number):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def convert(word):
    d = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    word_arr = list(word)
    number_arr = [d[el] for el in word_arr]

    while len(number_arr) != 5:
        number_arr.append('0')

    return int(''.join(number_arr))


def solution(word):
    ## make all possible cases into list
    arr = []
    numbers_ = ['1', '2', '3', '4', '5']
    numbers = ['0', '1', '2', '3', '4', '5']

    for d1 in numbers_:
        for d2 in numbers:
            if d2 == '0':
                arr.append(int(d1 + d2 + d2 + d2 + d2))
                continue
            for d3 in numbers:
                if d3 == '0':
                    arr.append(int(d1 + d2 + d3 + d3 + d3))
                    continue
                for d4 in numbers:
                    if d4 == '0':
                        arr.append(int(d1 + d2 + d3 + d4 + d4))
                        continue
                    for d5 in numbers:
                        arr.append(int(d1 + d2 + d3 + d4 + d5))

    print(arr)
    ## target word -> target number
    number = convert(word)
    print(f"word:{word}")
    print(f"number:{number}")
    ## binary search
    answer = binary_search(arr, number)
    answer += 1
    return answer


print(solution('AEE'))
