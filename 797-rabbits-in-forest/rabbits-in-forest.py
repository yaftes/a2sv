class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for ele in count:
            if count[ele] <= ele + 1:
                ans += ele + 1
            elif count[ele] % (ele + 1) == 0:
                ans += (count[ele] // (ele + 1) * (ele + 1))
            else:
                ans += ((count[ele] // (ele + 1)) + 1) * (ele + 1)
        return ans
        
        