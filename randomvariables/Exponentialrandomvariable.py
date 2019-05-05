import numpy as np
from .Generalrandomvariable import RandomVariable, NonPositiveException, LessThanOneException 

class Exponential(RandomVariable):
	def __init__(self, rate=1):
		"""
		Exponential random variable class
		
		Attributes:
		  rate (float) must be > 0, representing the rate parameter of the exponential distribution
		  mean (float) representing the mean value of the distribution
		  stdev (float) representing the standard deviation of the distribution
		"""
		if rate <= 0:
			raise NonPositiveException('Value of rate parameter must be greater than zero')
		self.rate = rate
		RandomVariable.__init__(self, 1/rate, 1/rate)

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

	def get_rate(self):
		"""
		Returns the rate parameter
		"""
		return self.rate

	def get_scale(self):
		"""
		Returns the scale parameter, which is equivalent to the mean
		"""
		return self.mean

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
			return np.random.exponential(self.get_mean())
		else:
			return np.random.exponential(self.get_mean(), n)

	def __repr__(self):
		return "Exponential({})".format(self.get_rate())
