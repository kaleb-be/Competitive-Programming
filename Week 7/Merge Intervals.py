class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        starts = [i[0] for i in intervals]
        ends = [i[1] for i in intervals ]
        starts.sort()
        ends.sort()
        start, end =starts[0],ends[0] 
        results = []

        for i in range(len(intervals)):
            try:
                if ends[i] < starts[i+1]:
                    results.append([start, end])
                    start = starts[i+1]
                end = ends[i+1]
            except IndexError: # in this case, we have reached the last element of starts and ends
                    results.append([start, end])
        
        return results
        
