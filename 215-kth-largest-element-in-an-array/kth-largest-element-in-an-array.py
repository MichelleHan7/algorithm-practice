class Solution:
    def partition(self, nums, left, right):
        i = randint(left, right)
        pivot = nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        i = left + 1
        j = right

        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j        

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left = 0
        right = n - 1
        while True:
            i = self.partition(nums, left, right)
            if i == target:
                return nums[i]
            elif i > target:
                right = i - 1
            else:
                left = i + 1
                