#string

s = "I am a string."
print(type(s))	#will say string

#boolean

yes = True	#Boolean True
print(type(yes))

no = False	#Boolean False
print(type(no))

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")	#will add "d" to end of list
print(alpha_list)	#will print list

#tuple -- ordered and changeable

alpha_tuple = ("a", "b", "c") 	#tuple initialization
print(type(alpha_tuple))	#will say tuple

try:						#attempt the following line
	alpha_tuple[2] = "d"
except TypeError:		#when we get a TypeError
	print("We can't add elements t tuples!")	#print this message
print(alpha_tuple)