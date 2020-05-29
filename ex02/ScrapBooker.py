import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        starty = position[0]
        startx = position[1]
        cropy = dimensions[0]
        cropx = dimensions[1]
        if (array.shape[0] >= (cropy + starty)) and (array.shape[1] >= (startx + cropx)):
            gr = array[starty:starty+cropy, startx:startx+cropx]
        else:
            raise ValueError("Crop value not in image frame")
        return(gr)

    def juxtapose(self, array, n, axis):
        result = array
        for r in range(n):
            result = np.concatenate((result, array), axis)
        return(result)

    def mosaic(self, array, dimensions):
        return(np.tile(array, dimensions))

    def thin(self, array, n, axis):
        if axis == 1:
            axis = 0
        else:
            axis = 1
        return(np.delete(array, slice(n-1, len(array), n), axis))


'''
finarr = []
arr = list("ABCDEFGHIJKL")
for x in arr:
    finarr.append(arr)
n_arr = np.array(finarr)
#print(n_arr)

obj = ScrapBooker()
crop = obj.juxtapose(n_arr, 2, 0)
print(crop)
crop = obj.thin(crop, 3, 0)
print(crop)
'''
