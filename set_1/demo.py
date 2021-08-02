"""
    Return the smallest possible int that is not already in the list
"""
def solution(A):
    #print('---')
    #print(A)
    l = filter(lambda x: x>0, A)
    l_st = set(l)
    l = list(l_st)
    #print (l)

    if not l:
        return 1

    l.sort()

    #if 1 not in l:
        #return 1

    if l[0] > 1:
        return 1

    if len(l) == max(l):
        return max(l) + 1

    l.reverse()

    while True:
        x = l.pop()
        if x+1 not in l:
            return x+1

def main():
    l0 = [-100, -50]
    l1 = [-23, -5, 0]
    l2 = [3,2,1]
    l3 = [1,3,6,4,1,2]
    l4 = [1,2,3]
    l5 = [-1,3]
    l6 = [22,10,7,11]

    print (solution(l0))    # 1
    print (solution(l1))    # 1
    print (solution(l2))    # 4
    print (solution(l3))    # 5
    print (solution(l4))    # 4
    print (solution(l5))    # 1
    print (solution(l6))    # 1

if __name__ == "__main__":
    main()
