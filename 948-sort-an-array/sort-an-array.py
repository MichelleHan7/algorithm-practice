
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            # Merge two sorted arrays
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # One of the arrays is now exhausted
            # Append all remaining elements from the other array
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        return mergeSort(nums)
