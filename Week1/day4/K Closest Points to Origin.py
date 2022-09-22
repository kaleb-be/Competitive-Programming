class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ordered_points = []
        for i in range(len(points)):
            point = points[i]
            distance = (point[0] ** 2) + (point[1] ** 2)
            pointer=0
            for j in range(len(ordered_points)):
                if ordered_points[j][0]<=distance:
                    pointer+=1
            ordered_points.insert(pointer, [distance, point])
        return [ordered_points[i][1] for i in range(k)]

    
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(Solution().kClosest(points,k))
