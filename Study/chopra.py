import numpy as np
import csv 

app ="Instagram"
minutes =[]

with open ("digital_behaviour.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader :
        minutes.append(int(row["Instagram_Minutes"])) #append the Instagram_Minutes column to the list
insta_array = np.array(minutes[:7:1])
sum = insta_array.sum()
avg = insta_array.mean()
min_value = insta_array.min()
max_value = insta_array.max()
print(insta_array)
#indexing
print(insta_array[0])
#vectors
print(insta_array[-1])

#slicing
print(insta_array[0:3])

#slicing with step
print(insta_array[1:-3])

#insta_array = [val/60 for val in insta_array]

valie = insta_array[insta_array>100]



