import numpy as np
import sys 

#now define a function that returns a value
def expo(x):
	return np.exp(x) 	#returns the np e^x function 

#now define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))
		
#define a main function 
def main():
	n = 10 #provides a default value for n 
	
	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument was provided usi it for n 
	
	show_expo(n) 	#call the show_expo subroutine
	
	
#run the main function 
if __name__ == "__main__":
	main()