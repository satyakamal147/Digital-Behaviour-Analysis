#join method
#split method

#Iteratives 


#iterables



#yield


#Ellipsis   
...
#Spread operator(Java Script)
a = [1,2,3] 

#Packing and Unpacking(Python)
b = (4,5,6)
c = {7,8,9} 


#filter function
#s= "GRIET College Nizampet Hyderabad"
#filtered = filter(lambda x: x.isalpha(), s.split())
  
#ans = " ".join(word[::-1] for word in s.split())
#res = "-".join(word[::-1] for word in input().split())
#print(ans)
#print(res)

#pick every alternate odd number from given input of using one line code
#odd_numbers = [int(x) for x in input().split() if int(x) % 2 == 1] 
#alternate_odd_numbers = odd_numbers[::2]

s = input().split()
odd_numbers = [int(x) for x in s if int(x) % 2 == 1]

#k= [int(num) for num in input().split() if num&1]
#k= list(filter(lambda x: x % 2 == 1, map(int, input().split())))
#k= list(filter(lambda x: x % 2 == 1, int(x) for x in input().split()))

#lambda function known as anonymous functions
#single use function 
#single line definition
#must return single line



#map function
#mapped = list(map(lambda x: x * 2, odd_numbers))

#list comprehension


#numpy
import numpy as np
