"""
    Find # of consecutive sequences of numbers in A
    having arithmetic mean of S
"""

def solution(A, S):
    success = 0
    for i in range(len(A)):
        segment = A[i:]
        total = 0
        cnt = 1
        for n in segment:
            total += n
            if total == cnt*S:
                success +=1
                # print (f'{cnt}')
                # print (f'{n}')
                # print ('--')
                if success == 1000000000:
                    break
            cnt += 1

        if success == 1000000000:
            break

    return success


def main():
    A = [2, 1, 3]
    S = 2
    print (solution(A, S))
    print ('====')
    A = [0, 4, 3, -1]
    S = 2
    print (solution(A, S))
    print ('====')
    A = [2, 1, 4]
    S = 3
    print (solution(A, S))
    print ('====')


    A = [5, 9, 2, 10, 12, 2, 4]
    S = 7
    print (solution(A, S))


if __name__ == '__main__':
    main()