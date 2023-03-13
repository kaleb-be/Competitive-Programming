class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_list = sorted(list(freq_map.values()), reverse=True)
        count = 0
        total = 0
        for freq in freq_list:
            count += 1
            total += freq
            if total >= len(arr) // 2:
                return count
        return len(freq_list)
