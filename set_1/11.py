"""
    Find the largest circle that does not contain any duplicate tags
"""
from math import hypot


def solution(S, X, Y):
    radii = list(map(hypot, X, Y))
    tags = list(zip(radii, S))
    tags.sort()
    print (tags)

    found_tags = []
    found_circles = []
    for i in tags:
        if i[1] in found_tags:
            exclude = i[0]
            break
        found_tags.append(i[1])
        found_circles.append(i)

    final_circles = list(filter(lambda x: x[0] != exclude, found_circles))

    return len(final_circles)


def main():

    S = "ABDCA"
    X = [2, -1, -4, -3, 3]
    Y = [2, -2, 4, 1, -3]
    print (solution(S, X, Y))       # 3

    print('---')

    S = 'ABCDBE'
    X = [1, 2, 3, -3, 3, 4]
    Y = [1, 2, 3, -3, -3, 4]
    print (solution(S, X, Y))       # 2

    print('---')

    S = 'ACFHEF'            # E and the second F occur at the same radius, so E should be excluded
    X = [1, 2, 3, 4, 5, 5]  # it's tricky bc "E" sorts alphabetically before "F"
    Y = [1, 2, 3, 4, 5, 5]
    print(solution(S, X, Y))        # 4


if __name__ == '__main__':
    main()
