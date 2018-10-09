import numpy as np 

def main():
	i = 0  #declares i is equal to o
	n = 10 #declares n is equal to 10
	x = 119.0 #float x, these have a .
	
	#we are using np to quickly use arrays 
y = np.zeros(n,dtype=float) #declares 10 zeros in this array

#we can use for loops to iterate through a variabe
for i in range(n): #i in range [0,n-1]
	y[i] = 2.0 * float(i) + 1.0 #sets y + 2i+1 
	
	#we can iterate through the y elements one by one
	for y_element in y: 
		print(y_element)
		
#execute the main function 
if __name__ == "__main__":
	main()