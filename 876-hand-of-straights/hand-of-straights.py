class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        hand.sort()
        for num in hand:
            if cnt[num]:
                cnt[num] -= 1
                k = groupSize - 1
                while k > 0:
                    if cnt[num+1] == 0:
                        return False
                    cnt[num+1] -= 1
                    num += 1
                    k -= 1

        return True