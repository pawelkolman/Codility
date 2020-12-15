def solution(A):
    # make array filled with False values, for later checking of their presence
    values = [False] * (len(A) + 1)

    # mark present values
    for value in A:
        values[value - 1] = True

    # iterate through array looking for the missing value
    for i in range(1, len(values)):
        if not values[i]:
            return i + 1

    # special case if array is empty
    return 1
