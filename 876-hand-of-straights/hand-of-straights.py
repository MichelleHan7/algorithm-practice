class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand.sort()
        cnt = Counter(hand)

        for num in hand:
            if cnt[num]:
                for _ in range(groupSize):
                    if not cnt[num]:
                        return False
                    cnt[num] -= 1
                    num += 1
        
        return True
            