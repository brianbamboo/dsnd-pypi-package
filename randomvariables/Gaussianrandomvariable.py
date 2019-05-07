import numpy as np
from .Generalrandomvariable import RandomVariable, NonPositiveException, LessThanOneException 

class Gaussian(RandomVariable):

	def __init__(self, mu=0, sigma=1):
		"""
		Gaussian random variable class
		
		Attributes:
		  mean (float) representing the mean value of the distribution
		  stdev (float) must be > 0, representing the standard deviation of the distribution
		"""
		RandomVariable.__init__(self, mu, sigma)

	def get_mean(self):
		"""
		Returns the mean attribute
		"""
		return self.mean

	def get_variance(self):
		"""
		Returns the variance, which is the stdev attribute squared
		"""
		return self.stdev ** 2

	def get_stdev(self):
		"""
		Returns the stdev attribute
		"""
		return self.stdev

	def generate(self, n=1):
		"""
		@param n (int > 1) number of random numbers to generate from this random variable
		@return a single randomly generated number (float) or a list of randomly generated floats
		"""
		if n < 1:
			raise LessThanOneException('x must be greater than or equal to 1')
		elif type(n) != int:
			raise TypeError("n must be an integer value")
		elif n == 1:
			return np.random.normal(self.get_mean(), self.get_stdev())
		else:
			return np.random.normal(self.get_mean(), self.get_stdev(), n)

	def __repr__(self):
		return "Gaussian({}, {})".format(self.get_mean(), self.get_variance())


