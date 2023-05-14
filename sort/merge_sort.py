import random

def merge_sort1(arr_1, arr_2):
    """ given two sorted lists, sort into one list containing both elements """
    nums = []

    ptr1, ptr2 = 0, 0
    while ptr1 < len(arr_1) and ptr2 < len(arr_2):
        if arr_1[ptr1] < arr_2[ptr2]:
            nums.append(arr_1[ptr1])
            ptr1 += 1
        else:
            nums.append(arr_2[ptr2])
            ptr2 += 1
        

    while ptr1 < len(arr_1):
        nums.append(arr_1[ptr1])
        ptr1 += 1
    while ptr2 < len(arr_2):
        nums.append(arr_2[ptr2])
        ptr2 += 1
    return nums


def merge_sort(arr):
    """ given a singular unsorted arr, sort """
    if len(arr) > 1:
        """ split into two different arrays """
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        """ now sort into arr """
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1




nums1 = [1, 2, 3, 6, 9]
nums2 = [3, 4, 5, 8]
print(merge_sort1(nums1, nums2))

nums = [random.randint(1, 50) for num in range(10)]
merge_sort(nums)
print(nums)

