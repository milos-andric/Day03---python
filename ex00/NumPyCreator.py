import numpy

class NumPyCreator:
	def from_list(lst):
		return (np,array(lst))
	
	def from_tuple(lst):
		return (np,array(lst))

	def from_iterable(lst):
		
		return(np,array(lst))

	def from_shape(shape):
		return(np.zeros(shape))

	def random(shape):
		return(np.random.rand(shape))

	def identity(num)
	return(np.identity(num))