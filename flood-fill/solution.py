class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        stack = [[sr,sc]]
        sameval = image[sr][sc]
        image[sr][sc] = newColor

        while stack:
            x,y = stack.pop(0)

            if x-1>=0 and image[x-1][y] == sameval:
                image[x-1][y] = newColor
                stack.append([x-1,y])
            if x+1<len(image) and image[x+1][y] == sameval:
                image[x+1][y] = newColor
                stack.append([x+1,y])
            if y-1>=0 and image[x][y-1] == sameval:
                image[x][y-1] = newColor
                stack.append([x,y-1])
            if y+1<len(image[0]) and image[x][y+1] == sameval:
                image[x][y+1] = newColor
                stack.append([x,y+1])

        return image
