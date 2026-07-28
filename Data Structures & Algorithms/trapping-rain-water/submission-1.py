class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        if n == 0:
            return 0

        left = 0
        right = n-1
        water = 0
        left_max = right_max = 0

        while left < right:
            
            if height[left] < height[right]:
                if left_max > height[left]:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return water

