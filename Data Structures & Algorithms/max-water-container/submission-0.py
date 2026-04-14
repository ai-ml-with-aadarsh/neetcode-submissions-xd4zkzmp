class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        len_heights = len(heights)
        
        for i in range(len_heights-1):    
            for j in range(len_heights):
                # area = l *  b
                l = heights[i] if heights[i] < heights[j] else heights[j]
                b = j - i
                area = l * b
                if area > max_area:
                    max_area = area

        return max_area