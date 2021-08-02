"""
    Calculate overall score for all tests
    Consolidate subtest results into a single value
"""

from math import ceil

def rtl(s):
    # remove trailing letters
    if s[len(s) - 1] in [*'0123456789']:
        return s
    else:
        s = s[:len(s) - 1]
        ss = rtl(s)

    return ss


def solution(T, R):
    T_new = list(map(rtl, T))
    comb = list(zip(T_new, R))
    d = {}
    for i, j in comb:
        if i not in d:
            d.update({i: {j}})
        else:
            d[i].add(j)

    tests = len(d)
    correct = 0
    for v in d.values():
        if v == {'OK'}:
            correct += 1

    # print (f'tests: {tests}')
    # print (f'correct: {correct}')
    score = ceil(correct * 100 / tests)
    return score


def main():
    T = ['test1', 'test2', 'test3', 'test4a', 'test4b']
    R = ["wrong", "OK", "OK", "error", "OK"]
    print (solution(T,R))

    print('========')
    T = ['test1',
         'test2',
         'test3a',
         'test3b',
         'test4',
         'test5a',
         'test5b',
         'test5c'
         ]

    R = ['OK',
         'Wrong answer',
         'OK',
         'OK',
         'Time limit exceeded',
         'OK',
         'OK',
         'Runtime error'
         ]

    print (solution(T,R))


    print ('========')
    T = ['test1',
             'test2a',
             'test2aa',
             'test333',
             'test4',
             'test5',
             'test6a',
             'test6bb'
             ]

    R = ['Wrong answer',
         'OK',
         'OK',
         'OK',
         'Runtime error',
         'OK',
         'OK',
         'Time limit exceeded'
         ]

    print (solution(T,R))


if __name__ == '__main__':
    main()