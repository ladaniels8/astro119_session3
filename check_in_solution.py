#include the numpy library
import numpy as np 

#define the main function
def main():

	i = 0
	x = 119.0
	
	for i in range(120): 
		if((i%2)==0):
			x += 3.
		else:
			x -= 5.
			
	s = "%3.2e" % x 
	
	
	print(s)
	
#now the rest of the program continues

if __name__ == "__main__": #if it exists then run it
	main()