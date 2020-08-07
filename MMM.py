import math
import random
import sys

def search(e, arr):
    c = 0
    for x in arr:
        if(e == x):
            return c
        else:
            c+=1
    return -1
# end function

def mean(arr):
    sum = 0
    c = 0
    for x in arr:
        sum += x
        c+=1
    return sum/c 
# end function

def median(arr):
    c = (len(arr)/2)+.5
    if type(c) != int:
        x1 = math.floor(c)
        x2 = math.ceil(c)
        return (x1+x2)/2
    else:
        return arr[c]
# end function

def mode(arr):
    arrVal = []
    arrCount = []
    for x in arr:
        i = search(x, arrVal)
        if(i>=0):
            arrCount[i] += 1
        else: 
            arrVal.append(x)
            arrCount.append(1)
    # end for loop
    c = 0
    i = 0
    for x in arrCount:
        if(x > arrVal[c]):
            c = i
    return arrVal[c]
# end function

def createDataSet(size, min, max):
    d = []
    for x in range(size):
        d.append(random.randint(min,max))
    return d
# end function

data = [72,22,84,52,11,37,36,63,46,46,95,57,74,10,94,96,55,66,24,3,5,72,77,68,2,60,48,39,42,45,58,51,1,28,97,12,8,25,93,61,12,17,15,79,29,37,22,20,6,31,15,78,32,19,46,9,38,2,27,93,25,83,20,96,22,37,80,52,3,30,43,88,92,67,41,6,41,46,97,23,58,47,49,41,60,32,47,94,73,96,30,28,18,60,82,79,48,31,49,91]

while True:
    print("welcome to the MMM system.")
    print("Do you want to use")
    print("1. a pregenrated data set")
    print("2. a Random data set")
    print("3. a manually inputed data set")
    print("4. a data file")

    choice = int(input())
    if (choice > 4)or(choice < 1):
        print("that choice is incorrect, please choose again")
    else: 
        break
# end while

if choice == 2:
    while True:
        print("how big of a sample size?")
        sz =  int(input())
        if(sz>0):
            break

    while True:
        print("What is the minimum value?")
        mi =  int(input())
        if(mi>0):
            break

    while True:
        print("What is the Maximum value?")
        ma =  int(input())
        if(ma>mi):
            break

    data = createDataSet(sz,mi,ma)

if choice == 3:
    data = []
    print("input numbers. to end type input a 'q'")
    while True:
        d = input()
        if d == 'q':
            break
        data.append(int(d))
    
if choice == 4:
    print("this choice has not been Implemented yet")
    sys.exit()

print("Mean: "+str(mean(data)))
print("Mode: "+str(mode(data)))
print("Median: "+str(median(data)))