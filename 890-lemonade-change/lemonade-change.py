class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {
            5: 0,
            10: 0,
        }

        for bill in bills:
            if bill == 5:
                freq[5] += 1
            elif bill == 10:
                if freq[5] < 1:
                    return False
                freq[5] -= 1
                freq[10] += 1
            elif bill == 20:
                if freq[10] > 0 and freq[5] > 0:
                    freq[10] -= 1
                    freq[5] -= 1
                elif freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False
        return True
