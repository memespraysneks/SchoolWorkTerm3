def merge(left, right):
    merged = []
    size_left = len(left)
    size_right = len(right)
    i = 0
    j = 0
    # if not left:
    #     return right
    # if not right:
    #     return left
    while i < size_left and j < size_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while j < size_right:
        merged.append(right[j])
        j += 1
    while i < size_left:
        merged.append(left[i])
        i += 1

    return merged

# def merge(left,right):
#     merged = []
#     size_left = len(left)
#     size_right = len(right)
#     i = 0
#     j = 0
#     while i < size_left or j < size_right:
#         if i == size_left:
#             merged.append(right[j])
#             j += 1
#         elif j == size_right:
#             merged.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     return merged

def merge_tooeasy(left, right):
    return sorted(left + right)