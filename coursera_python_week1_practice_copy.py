#Practice questions based on the Python Data Science Coursera Course
#And Python Data Science Handbook https://jakevdp.github.io/PythonDataScienceHandbook/

# A) Import numpy, check the version, get a list of all the functions it offers

# 1) Create a list

# 2) Convert the list into an array

# 3) Create a 1D array without first creating a list

# 4) Create an array directly with a 2 X 3 dimensionality of a float 32 data type
# and find the array's number of dimentions, size of each dimension, total elements,
# byte size of each element, and total size of elements

# 5) create a 3 X 4 array filled with 3.5, one with random normally distributed values with a mean of
# 5 and sd of 2, and one with uniformly distributed random values between 0 and 1

# 6) Use a numpy function to return one array of  4 evenly spaced values between
# 0 and 1 and then one of evenly spaces of 3 values between 2 and 30

##########
#Answers 1 - 6
##########

#A
#  Import numpy, check the version, get a list of all the functions it offers
import numpy as np
np.__version__
dir(np)
#creating a list and then converting it into an array
#1
list1 = [1, 2, 3]

#2
array1 = np.array(list1)
array1

#3
#creating an array directly
array2 = np.array([4, 5, 6])

#4
#creating an 2 x 3 array
array3 = np.array([[7, 8, 9], [10, 11, 12]], dtype = 'float32')
array3
# number of dimentions
array3.ndim
# size of each dimension
array3.shape
# total elements
array3.size
# byte size of each element
array3.itemsize
# total size of elementsarray3.shape
array3.nbytes

#5
#3 X 4 array filled with 3.5
np.full((3, 5), 3.5)
#Array with random normally distributed values with a mean of 5 and sd of 2
np.random.normal(5, 2, (3, 5))
#Array with uniformly distributed random values between 0 and 1
np.random.random((3, 5))

#6
#Array of  4 evenly spaced values between 0 and 1
np.linspace(0, 1, 4)
#Array of evenly spaces of 3 values between 2 and 30
aranged1 = np.arange(2, 30, 3)
aranged1

# 7) Change the second array into a 2 x 5 array temporarily

# 8) Change the array into a 2 x 5 array perminentaly with a different function
# and use the index notation to change the final value to 34

# 10) Create two 3 x 2 arrays with single function, one full of 1s, the other 0s

# 11) Use a function to create a identity matrix (array where all elements are equal to zero,
# except for the k-th diagonal, whose values are equal to one)

# 12) Take the first array and create an array where all elements are equal to
# zero except for the k-th diagnol, whose values are equal to the array numbers

# 13) Use a numpy function to create an array that repeats 1, 2, 3 three times in a row
# but only write the order of numbers once

# 14) Use a function to create an array of 1, 1, 1, 2, 2, 2, 3, 3, 3
# but only write the order of numbers 1, 2, 3 once, then split into 3 arrays
# the first containing the first 3 numbers, 2nd the 4th and 5th, and 3rd the rest


#########
#Questions 7 to 14
#########

#7
aranged1 = aranged1.reshape(2, 5)
aranged1

#8
aranged2 = np.arange(2, 30, 3)
aranged2.resize(2, 5)
aranged2
#using the index notation to change the final value to 34
aranged2[-1, -1] = 34
aranged2

#10
np.ones((3, 2))
np.zeros((3, 2))

#11
np.eye(3)

#12
np.diag(array1)

#13
np.array([1, 2, 3] * 3)

#14
arepeated = np.repeat([1, 2, 3], 3)
a1, a2, a3 = np.split(arepeated, [3, 5])
print(a1, a2, a3)
#########
#Questions 15 to 30
#########
# 15) Create a 3 x 4 array of 1s, but make them integers,
# The split into 3 arrays
aones = np.ones([3, 4], int)

aones = np.arange(10)
a1, a2, a3 = np.split(aones, [3, 5])
print(a1, a2, a3)

# 16) concatenate the above array verticly, then horizontally with itself
np.vstack([aones, aones])
np.hstack([aones, aones])
# 18) Create a function that adds two numbers with an optional 3, and a flag
# that prints Flag Is True when it's set to true
def fun_add (x, y, z = None, flag = False):
    print(x + y +z)
# 19) Create a tuples with the number 1, 2, 3, a, and demonstrate that it's a type
# tuple

# 20) Create a list with the numbers 1, 2, 3, a and then append 4 to it

# 21) Write a for-loop to iterate over the list and print each variable

# 22) Write a while loop using the indexing oporator starting at position 0, and
# printing each variable in the list until reaching the end

# 23) Concatonate the tuple 1, 2 with a, b

# 24) Create a list with three 1s, writing 1 only once

# 25) check set membership for the numbers 8 and 1 are in the list

# 26) Slice the first three numbers in the list

# 27) Create a string with the words 'dog' and 'cat', print the penultimate

#letter and the one before that slicing with negative numbers, and check set
#membership for the word 'dog'

# 28) Split the list and select the first, and then last word from it, and also
#create a list with each word as a variable

# 29) Create a dictionary with the key-value pairs of pets-dog, food-berry,
#drink-water, then call the value berry

# 30) Iterate over all the keys and print out the values, then iterated over the
#values and print them out again, and then print both

########
#Answers 15 - 30
#######
#15
%timeit aones = np.ones((3, 4), int)
%time aones = np.ones((3, 4), int)
#16
#Concatenate the above array verticly, then horizontally with itself
np.vstack([aones, aones])
np.hstack([aones, aones])
# 18
def add_numbers (x, y, z = None, flag = False):
    if (flag):
        print('Flag is true!')
    if (z == None):
        return x + y
    else:
        return x + y + z

add_numbers(1, 2, flag = True)
add_numbers(1, 2, 3)

#19
tuple1 = (1, 2, 3, 'a')
tuple1
type(tuple1)

#20
list1 = [1, 2, 3, 'a']
list1.append(4)
list1

#21
for v in list1:
    print(v)

#22
i = 0
while (i != len(list1)):
    print(list1[i])
    i = i + 1

#23
(1, 2) + ('a', 'b')
#This works even with tuples because python isn't changing the original tuple
#just creating a new one in memory
tuple1 + (1, 2)


#24
#With a tuple you get a number output and not another tuple
[1] * 3
(1) * 3

#25
8 in list1
1 in list1

#26
list1[0:3]

#27
string1 = 'dog cat'
print(string1[-4:-1])
print('dog' in string1)

#28
string1.split(' ')[0]
string1.split(' ')[1]
string1.split(' ')

#29
dictionary1 = {'pets': 'dog', 'food': 'berry', 'drink': 'water'}
dictionary1['food']

#30
for k in dictionary1:
    print(dictionary1[k])

for v in dictionary1.values():
    print(v)

for k, v in dictionary1.items():
    print(k)
    print(v)


# 31) add to the dictionary the key best with a none value
# 32) create a list with the words dog, cat, and mouse, and unplack them into
#canine, feline, and rodent
# 33) Create a dictionary with a single value for the keys name, num_purchased, price
#then write a sales staement string with these items, and call the format method
#on the string and pass the dictionary values in
# 34) Import the mpg dataset as a list of dictionaries (one per row) after examining and changing
#the working directory and using python magic to change the floating point precision to 2
# 35) Get CSV column names and the number of dictionaries in the dataset
# 36) Find mean city fuel economy across all cars
# 37) Find unique values for numer of cylinders of the cars
# 38) Iterate over the dictionaries to output a list of tuples with the mean city
#mpg per cylinder type
# 39) Retun current time in seconds since the epoch, the local date, and the date
#10 days ago

#31
dictionary1['best'] = None
dictionary1

#32
list2 = ['dog', 'cat', 'mouse']
canine, feline, rodent = list2
canine
feline
rodent

#33
dictionary2 = {'name': 'pika', 'num_purchased': 5, 'price': 3.2}
statement1 = '{} bought {} items, for a total of ${}'
statement1.format(dictionary2['name'],
                    dictionary2['num_purchased'],
                    dictionary2['price'] * dictionary2['num_purchased'])

#34
import os
import pandas as pd
os.getcwd()
os.chdir("C:/Users/Aria/Documents/ds_practice/Python/course1_downloads/")
import csv
%precision 2
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
mpg[:3]

    # mpg : miles per gallon
    # class : car classification
    # cty : city mpg
    # cyl : # of cylinders
    # displ : engine displacement in liters
    # drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
    # fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
    # hwy : highway mpg
    # manufacturer : automobile manufacturer
    # model : model of car
    # trans : type of transmission
    # year : model year

#35
mpg[0].keys()
len(mpg)

#36
#iterating over each dictionary in the list
#pulling the city mpg string for it
#converting that string into a float, summing it, and dividing by total number of
#variables
sum(float(dict['cty']) for dict in mpg) / len(mpg)

#37
set(dict['cyl'] for dict in mpg)

#38
city_mpg_by_cyl = []

for c in set(dict['cyl'] for dict in mpg):
#for each cylinder level when you go to the top of the for loop you need to set those variables equal to 0 otherwise they will carry the values from the previous cylinder level (as you iterate through the cylinder levels) which is not what you want.
    sum_mpg = 0
    cyl_count = 0
    for dict in mpg:
        if dict['cyl'] == c: #grouping by cylinder levels
            sum_mpg += float(dict['cty']) #adding the city mpg to the sum
            cyl_count += 1 #additing 1 to the count
    city_mpg_by_cyl.append((c, sum_mpg / cyl_count)) #appending the tuple

city_mpg_by_cyl

#39
import datetime as dt
import time as tm
tm.time()
dt.date.today()
dt.date.today() - dt.timedelta(days = 10)

# 40) Convert current time in seconds since the epoch to a datetime, and extracy year,
#month, day, hour, minute, and second from it
# 41) Create a class called dog, where the default for name_origin is pokemon, and
# write two methods, set_name and was_adopted that will change instance bound variables
# called set_name, and was_adopted respectively. Then instantiate the class by calling
# the class name with empty parenthesis behind it.
# 42) Using map find the highest price between every pair of items between the following
# two lists: 1, 5, 7, 9 and 1, 3, 7, 10
# 43) Create a lambda where a and b are added
# 44) Create a list with even numbers between 0 and 10, once with a for loop and
# once with a list comprehension
# 45) Transpose an array
# 46) Exampine the array data type, and cast it to a different type
# 47) Find the sum, maximum, minimum, mean, and SD of an array, as well as the index
# for the maximum and minimum values
# 48) Create an array using a function with the squares of the numbers 0 through 10,
# then pull the values at the first and last index, as well as the last 4 numbers
# 49) Create a 6 x 6 array with the number 0 to 35, and then select from it the
# 3rd and 4th rows and columns

#40
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow
dtnow.year
dtnow.month
dtnow.day
dtnow.hour
dtnow.minute
dtnow.second

#41
class Doggo:
    name_origin = 'Pokemon'

    def set_name(self, new_name):
        self.name = new_name
    def set_adopted(self, adoption_status):
        self.adopted = adoption_status

doggo = Doggo()
doggo.set_name('Pikachu')
doggo.set_adopted('Yes')
print('Was {}, named after a {}, adopted? {}'.format(doggo.name, doggo.name_origin, doggo.adopted))

#42
mapped1 = map(max, [1, 5, 7, 9], [1, 3, 7, 10])
for maxed in mapped1:
    print(maxed)

#43
lambda_fun = lambda a, b: (a + b)
lambda_fun(8, 9)

#44
list4 = []
for number in range(0, 10):
    if number % 2 == 0:
        list4.append(number)
list4

list5 = [number for number in range(0, 10) if number % 2 == 0]
list5

#45
array3.shape
array3
array4 = array3.T
array4.shape
array4

#46
array4.dtype
array5 = array4.astype('int64')
array5.dtype

#47
array5.sum()
array5.max()
array5.min()
array5.mean()
array5.std()
array5.argmax()
array5.argmin()

#48
array6 = np.arange(11) ** 2
array6
array6[0], array6[-1], array6[-4:]

#49
#Create a 6 x 6 array with the number 0 to 35
array7 = np.arange(36)
array7.resize((6, 6))
array7
#select from it the 3rd and 4th rows and columns
array7[2:4, 2:4]


# 50) Filter the array to select only numbers over 20, then assign all those numbers
# to be -7 in the original array

# 51) Duplicate the array in a way that changing the copy won't affect the original
# when converting all values in the copy into zero

# 52) Create a 4 x 5 array of random integers from 0 to 100

# 53) iterate over the array rows and print them out, then do the same for the row
# index, and then for both row and index

# 54) Create a new array with values twice as large as the previous array, then
# print out each row of the second array next to the row of the first array, followed
# by an array that is the addition of each corresponding value in each array

# 55) Create a 1D array with number from 0 to 9, then reverse every other number
# starting at the number 8 using slice notation




#50
array7[array7 > 20]
array7[array7 > 20] = -7
array7

array8 = array7.copy()
array8[:] = 0
array8
array7

#52
array_rand = np.random.randint(0, 101, (4, 5))
array_rand

#53
for array_row in array_rand:
    print(array_row)

for array_irow in range(len(array_rand)):
    print(array_rand[array_irow])

for array_irow, array_row in enumerate(array_rand):
    print('row', array_irow, 'is', array_row)

#54
array_rand2 = array_rand * 2
array_rand2
for i, j in zip(array_rand2, array_rand):
    print(i, j)
    print(i + j)

#55
#1D array with number from 0 to 9
#reversing every other number starting at the number 8 using slice notation
array1d = np.arange(10)
array1d
array1d[8::-2]
