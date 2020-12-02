def solution(A, K):
    """recursive solution"""

    # if array is empty or K is 0, just return A
    # else shift array 1 step and decrease K and pass recursively
    return A if K == 0 or A == [] else solution([A[-1]] + A[:-1], K - 1)


def smart_solution(A, K):
    """smart solution that uses the possibilities of python"""

    # decrease K if is bigger than array length
    K = K % len(A)

    # if array is empty, just return A
    # else return last K elements + left elements
    return A if A == [] else A[-K:] + A[:-K]
