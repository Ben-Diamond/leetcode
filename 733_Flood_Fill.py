class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        original_colour = image[sr][sc]

        queue = [(sr, sc)]

        if original_colour == color:
            return image

        image[sr][sc] = color
        while len(queue) > 0:
            newq = []
            #do not need to make a "visited" set because visiting a pixel changes its colour

            for pixel in queue:
                x, y = pixel
                for dx in (-1,1):
                    if x+dx == -1 or x+dx == len(image):
                        continue
                    if image[x+dx][y] == original_colour:
                        image[x+dx][y] = color
                        newq.append((x+dx, y))
        
                for dy in (-1,1):
                    if y+dy == -1 or y+dy == len(image[0]):
                        continue
                    if image[x][y+dy] == original_colour:
                        image[x][y+dy] = color
                        newq.append((x, y + dy))


            queue = newq.copy()

        return image

        





image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
solver = Solution()
print(solver.floodFill(image,sr,sc,color))