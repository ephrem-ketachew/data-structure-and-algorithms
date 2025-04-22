def merge(nums1, m, nums2, n):
    nums2Iterator = 0
    for nums1Iterator in range(len(nums1)):
        if nums1Iterator < m:
            if n > 0 and nums2Iterator < len(nums2) and nums1[nums1Iterator] > nums2[nums2Iterator]:
                for k in range(len(nums1) - 1, nums1Iterator, -1):
                    nums1[k] = nums1[k - 1]
                nums1[nums1Iterator] = nums2[nums2Iterator]
                nums2Iterator += 1
                m += 1
        else:
            for k in range(m, len(nums1)):
                nums1[k] = nums2[nums2Iterator]
                nums2Iterator += 1
            break