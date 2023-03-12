class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr)-1, 0, -1):
            # find the index of the maximum element in the unsorted part of the array
            max_index = arr.index(max(arr[:i+1]))
            if max_index != i:
                # if the maximum element is not already at the end of the unsorted part, flip the subarray to move it there
                if max_index != 0:
                    arr[:max_index+1] = arr[:max_index+1][::-1]
                    flips.append(max_index+1)
                # flip the entire unsorted part to move the maximum element to the end of the array
                arr[:i+1] = arr[:i+1][::-1]
                flips.append(i+1)
        return flips
