"""
    Find the smallest number of consecutive days to travel to all destinations
"""
def solution(A):
    destinations = set(A)

    trips = []

    for x in range(len(A)):
        visited = set()
        AA = A[x:]
        cnt = 1
        for i in AA:                # get rid of AA and just use A[x:] to avoid copy? or make an iterator over it? Check performance improvements
            if i not in visited:
                visited.add(i)
                if visited == destinations:
                    trips.append(cnt)
                    break
            cnt += 1

    return min(trips)
    
A = [7,3,7,3,1,3,4,1]
print (solution(A))

A = [2,1,1,3,2,1,1,3]
print (solution(A))

A = [7,5,2,7,2,7,4,7]
print (solution(A))
