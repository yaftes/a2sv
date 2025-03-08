class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = Counter(blocks[:k])
        min_ = window['W']
        for i in range(len(blocks) - k):
            window[blocks[i]] -= 1
            if window[blocks[i]] == 0:
                del window[blocks[i]]
            window[blocks[i+k]] = window.get(blocks[i+k],0) + 1
            min_ = min(min_,window['W'])
        return min_
        