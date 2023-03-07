"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

"""

class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        def fillColor(img, x, y, oldColor, newColor):
            if x >= len(img) or x < 0 or y >= len(img[0]) or y < 0:
                return
            if img[x][y] == oldColor:
                img[x][y] = newColor
            else:
                return
            
            fillColor(img, x + 1, y, oldColor, newColor)
            fillColor(img, x - 1, y, oldColor, newColor)
            fillColor(img, x, y + 1, oldColor, newColor)
            fillColor(img, x, y - 1, oldColor, newColor)
        if image[sr][sc] != color:
            fillColor(image, sr, sc, image[sr][sc], color)
        return image
if __name__ == "__main__":
    s = Solution()
    # data = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    data = [[0, 0, 0], [0, 0, 0]]
    #print(-2 >= len(data))
    print(s.floodFill(data, 1, 1, 0))
