def merge(left, right):
    ans = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1
    return ans

def mergesort(input):
    if len(input) <= 1:
        return input
    else:
        return merge(mergesort(input[:len(input)//2]), mergesort(input[len(input)//2:]))