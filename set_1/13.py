"""
    The list contains all 'a's and 'b's
    divide the list into 3 segments to where there are an equal number of 'a's in each segment
"""


def solution(S):
    N = S.count('a')
    # print (N)
    if not N % 3 == 0:
        return 0

    indices = []
    idx = 0

    for _ in range(N):
        i = S.index('a', idx)
        indices.append(i)
        idx = i+1

    # print (indices)

    w = int(N/3) - 1
    # print (w)
    x = w + 1
    # print (x)
    y = int(2*N/3) - 1
    z = y + 1
    # print (y)
    # print (z)

    w_index = indices[w]
    x_index = indices[x]
    y_index = indices[y]
    z_index = indices[z]
    # print (w_index)
    # print (x_index)
    # print (y_index)
    # print (z_index)

    return (x_index - w_index) * (z_index - y_index)


def main():
    S = 'abbbbabbbbba'
    print (solution(S))             # 30

    S = 'abbbabbbabbbbabbbbbabba'
    print (solution(S))             # 24

    S = 'babaa'
    print (solution(S))             # 2

    S = 'aaabaaa'
    print (solution(S))             # 1


if __name__ == '__main__':
    main()
