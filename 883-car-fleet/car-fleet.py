class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        posSpeed = [(p, s) for p, s in zip(position, speed)]
        posSpeed.sort()
        st = []

        for p, s in reversed(posSpeed):
            time = (target - p) / s 
            st.append(time)
            if len(st) >= 2 and st[-2] >= time:
                st.pop()
        
        return len(st)