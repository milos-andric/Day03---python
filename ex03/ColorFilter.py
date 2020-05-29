import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor:
	def __init__(self):
		pass

	def load(self, path):
		img = mpimg.imread(path)
		print("Loading image of dimensions " + str(np.shape(img)[0]) + " x " + str(np.shape(img)[1]))
		return(img)

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()


class ColorFilter:
	def __init__(self):
		pass

	def invert(self,array):
		for pixels in array:
			for color in pixels:
				color[0] = 1 - color[0]
				color[1] = 1 - color[1]
				color[2] = 1 - color[2]
				color[3] = 1
		return(array)
	
	def to_blue(self,array):
		for pixels in array:
			for color in pixels:
				color[0] = np.zeros(1)
				color[1] = np.zeros(1)
		return(array)

	def to_green(self,array):
		for pixels in array:
			for color in pixels:
				color[0] *= 0
				color[2] *= 0
		return(array)

	def to_red(self,array):
		for pixels in array:
			for color in pixels:
				color[1] -= color[1]
				color[2] -= color[2]
		return(array)

	def celluloid(self,array):
		lowest
		for pixels in array:
			for color in pixels:
				color[1] -= color[1]
				color[2] -= color[2]
		return(array)

Filter = ColorFilter()
imp = ImageProcessor()
arr = imp.load('./musk.png')
arr = Filter.to_red(arr)
imp.display(arr)