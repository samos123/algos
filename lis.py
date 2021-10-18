def lis_til(A, i):
    if i == 0: # only 1 element
        return 1
    answer = 1
    for j in reversed(range(i)):
        if A[j] < A[i]:
            answer = max(answer, 1 + lis_til(A, j))
    return answer

def lis_recursive(A):
    answer = 1
    for i in range(len(A)):
        answer = max(answer, lis_til(A, i))
    return answer

def lis_memoized(A):
    answer = 1
    cache = {0: 1}
    for i in range(len(A)):
        answer = max(answer, lis_til_memoized(A, i, cache))
    return answer
    
def lis_til_memoized(A, i: int, cache):
    if i in cache:
        return cache[i]
    answer = 1
    for j in reversed(range(i)):
        if A[j] < A[i]:
            answer = max(answer, 1 + lis_til_memoized(A, j, cache))
    cache[i] = answer
    return answer

def lis_dp(A):
    lis_til = [1] * len(A)
    answer = 1
    highest_index = -1
    for i in range(1, len(A)):
        highest = 1
        for j in range(i-1, -1, -1):
            if A[j] < A[i]:
                highest = max(highest, 1 + lis_til[j])
        lis_til[i] = highest
        if lis_til[i] > answer:
            highest_index = i
        answer = max(lis_til[i], answer)

    lis_seq = [A[highest_index]]
    prev_val = A[highest_index]
    credit = lis_til[highest_index]
    for j in range(highest_index-1, -1, -1):
        if lis_til[j] == credit - 1:
            lis_seq.insert(0, A[j])
            credit -= 1

    print("Input: %s, Highest index: %s, LIS: %s, Len: %s" % (A, highest_index, lis_seq, len(lis_seq)))
    return answer


fourteen =[ 64, 34, 56, 73, 52, 75, 51, 2, 78, 14, 10, 74, 36, 32, 31, 32, 87, 36, 4, 66, 89, 47, 12, 53, 9, 73, 34, 92, 34, 87, 1, 28, 24, 46, 92, 27, 1, 13, 75, 46, 4, 74, 93, 76, 56, 31, 42, 65, 58, 84, 61, 18, 59, 89, 29, 96, 101, 42, 95, 28, 65, 48, 51, 51, 18, 90, 43, 75, 22, 87, 100, 80, 14, 13, 78, 55, 78, 18, 25, 53, 88, 8, 9, 16, 86, 18 ]

def test_basic(method):
    assert method([1, 2, 3]) == 3, "%s([1, 2, 3]) should return 3" % (method.__name__)
    assert method([1, 2, 1, 5]) == 3, "%s([1, 2, 1, 5]) should return 3" % (method.__name__)
    assert method(fourteen) == 14, "%s(%s) should return 14" % (method.__name__, fourteen)

if __name__ == "__main__":
    test_basic(lis_recursive)
    test_basic(lis_memoized)
    test_basic(lis_dp)
    print("Everything passed")
