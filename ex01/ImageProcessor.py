import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor:
	def load(self, path):
		img = mpimg.imread(path)
		print("Loading image of dimensions " + str(np.shape(img)[0]) + " x " + str(np.shape(img)[1]))
		return(img)

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()


imp = ImageProcessor()
arr = imp.load('./img.png')
imp.display(arr)
