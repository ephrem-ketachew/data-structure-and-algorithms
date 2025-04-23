def mergeArrays(nums1, nums2):
    j = 0
    i = 0
    mergedArray = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i][0] < nums2[j][0]:
            mergedArray.append([nums1[i][0], nums1[i][1]])
            i += 1
        elif nums1[i][0] > nums2[j][0]:
            mergedArray.append([nums2[j][0], nums2[j][1]])
            j += 1
        else:
            mergedArray.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
            i += 1
            j += 1
    
    while i < len(nums1):
        mergedArray.append([nums1[i][0], nums1[i][1]])
        i += 1
    while j < len(nums2):
        mergedArray.append([nums2[j][0], nums2[j][1]])
        j += 1

    return mergedArray