# Time Complexity : O(n^2)
# Space Complexity : O(n) 

# Did this code successfully run on Leetcode : 
# YEs

# Any problem you faced while coding this : 

# Your code here along with comments explaining your approach

def floodFill(self, image, sr, sc, newColor):
        # time O(n^2) space O(n)
        # runtime: 90ms
        rows, cols = len(image), len(image[0])
        dir = ((-1,0),(1,0),(0,1),(0,-1))
        visited = set(); pixel = image[sr][sc] # store pixel value
        def dfs(i, j): 
            if (i,j) in visited: return
            visited.add((i,j)) 
            for d in dir: # traverse neighbors
                x, y = i+d[0], j+d[1] 
                if 0<= x < rows and 0<= y < cols and image[x][y] == pixel:
                    image[x][y] = newColor
                    dfs(x,y)
        if newColor != pixel: 
            image[sr][sc]=newColor
            dfs(sr, sc) 
        return image