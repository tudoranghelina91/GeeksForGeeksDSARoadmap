def maxArea(height):
    l = 0
    r = len(height) - 1
    d = r - l
    maxSurface = d * min(height[l], height[r])

    while l < r:
        d = r - l
        surface = d * min(height[l], height[r])
        maxSurface = max(surface, maxSurface)
        
        if height[l] < height[r]:
            l+=1
        else:
            r -= 1

    return maxSurface

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))