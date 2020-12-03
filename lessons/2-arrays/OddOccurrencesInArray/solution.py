def solution(A):
    """smart solution that uses the XOR principle"""

    unpaired_number = 0
    for number in A:
        unpaired_number ^= number

    return unpaired_number


def simple_solution(A):
    """simple solution"""

    # sort an array to align the same numbers next to each other
    A.sort()

    # jump 2 staps to check if the next number is the same
    for i in range(0, len(A), 2):
        if i + 1 == len(A) or A[i] != A[i + 1]:
            return A[i]
