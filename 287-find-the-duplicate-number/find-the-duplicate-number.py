class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        head = 0
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return head