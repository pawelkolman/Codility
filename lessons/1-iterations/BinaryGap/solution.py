def solution(N):
    """sexy solution"""

    # convert N to binary representation
    # strip possible zeros at the beginning or end of the number
    # split zeros strings divided by the ones
    # get max string from the array basing on its ASCII value
    # get length of the max string
    return len(max(format(N, 'b').strip('0').split('1')))


def iterable_solution(N):
    """iterable solution"""

    # convert decimal N to binary representation
    binary_representation = format(N, 'b')

    longest_gap = current_gap = 0

    for digit in binary_representation:
        # if current digit is 0, increase current gap
        if digit == '0':
            current_gap += 1
        # if current digit is 1, check if current gap is the longest one
        else:
            if current_gap > longest_gap:
                longest_gap = current_gap
            current_gap = 0

    return longest_gap
