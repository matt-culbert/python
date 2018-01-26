import numpy as np
import glob
'''
perform standard deviation and mean on the error ranks in the photos
compare to error_rank submitted by parent
'''

history = glob.glob('/home/pi/Desktop/camera/*.txt')

def calculate(error_rank, history):
	#perform standard dev on history 
	#check mean on history and check if error rank within bounds of mean

	calc1 = np.mean(history)
	calc2 = np.std(history)

	func1 = calc1 - calc2
	func2 = calc1 + calc2

	if error_rank > func2 or error_rank < func1:

		return True 

	else: return False