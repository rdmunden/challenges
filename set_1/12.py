"""
    Find the shortest compressed message by eliminating any 3 consecutive letters
"""


def solution(S, K):
    if len(S) <= K:
        return len(S)

    if len(S) == K+1:
        return 1

    if len(S) == K+2:
        return 2

    sizes = []

    # for debugging, save messages
    # messages = []

    for x in range(len(S)-K):
        s = [*S]
        s[x:x+K] = ''
        s = "".join(s)

        m = ''
        lastchar = ''
        count = 1
        for i in s:
            if i == lastchar:
                count += 1
            else:
                if count == 1:
                    count = ''
                m += str(count) + lastchar
                lastchar = i
                count = 1

        if count == 1:
            count = ''
        m += str(count) + lastchar

        # print (m)

        sizes.append(len(m))

        # for debugging, save messages
        # messages.append(m)


    min_size = min(sizes)

    # for debugging, print all the messages with the min size
    # print ("---")
    # final = list(zip(sizes, messages))
    # for i in final:
    #     if i[0] == min_size:
    #         print (i[1])

    return min_size


def main():
    K = 3
    S = "ABBBCCDDCCC"
    # [[('A', 1)], [('B', 3)], [('C', 2)], [('D', 2)], [('C', 3)]]

    print (solution(S,K))   # A3B4C + 1 more -> 5

    S = "ABBBCCDDCA"
    # [[('A', 1)], [('B', 3)], [('C', 2)], [('D', 2)], [('C', 1)], [('A', 1)]]

    print (solution(S,K))   # A3BDCA + 2 more -> 6

    S = 'ABCDDDDDCACDDDDD'
    # ABC5DCAC5D = 10
    # ABC10D = 6
    print (solution(S,K))   # ABC10D -> 6

    S = 'AACCCCCCCABDCCCCC'
    # AACCCCCCCABDCCCCC = 17
    # 2A7CABC5C = 9
    # AACCCCCCCCCCCC
    # 2A12C = 5
    print(solution(S, K))  # 2A12C -> 5


if __name__ == '__main__':
    main()

