def checkIfExist(arr):
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False
    # arr.sort()
    # for i in range(len(arr) - 1):
    #     double = arr[i] * 2
    #     begin = i + 1
    #     end = len(arr) -1
    #     while begin <= end:
    #         mid = (begin + end) // 2
    #         if arr[mid] == double:
    #             return True
    #         if double > arr[mid]:
    #             begin = mid + 1
    #         else:
    #             end = mid - 1

    # return False

print(checkIfExist([3,1,7,11]))