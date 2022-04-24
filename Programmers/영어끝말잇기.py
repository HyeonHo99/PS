def solution(n, words):
    count = -1
    last = words[0][0]
    d = dict()

    for i, word in enumerate(words):
        ## compare last and first
        if last != word[0]:
            count = i
            break

        ## update last <- first
        last = word[-1]

        ## check repetition
        if word not in d:
            d[word] = True
        else:
            count = i
            break

    if count == -1:
        answer = [0, 0]
    else:
        answer = [count % n + 1, count // n + 1]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# d = dict()
# d[0] = "a"
# d[1] = "b"
# print(0 not in d)
# print(2 in d)
# print("a" in d)