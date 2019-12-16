import random

class ECMPalgorithm:
	def load_path(self):
			some_list = ['S1','S2','S3','S4'] 					#use ECMP to implement the flow path
			probabilities = [0.25,0.25,0.25,0.25]

			x = random.uniform(0,1)  
			cumulative_probability = 0.0
			for item, item_probability in zip(some_list, probabilities):  
			    cumulative_probability += item_probability  
			    if x < cumulative_probability:break  
			path = item			
			return path
