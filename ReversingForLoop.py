import time

d = 1# D is some varible that you modify i by
i =0 

while i<10: #for(i=0;i<10;i+=d)
    print(i)# some fuction that Benefits from a reversing I value
    
    # change the d value
    # this is the key to the loop. instead of doing i++ in the for loop, you modify it by d and then change d when you want to reverse the loop.
    # This can also be changed to some other number to allow for a scaling changeing value. You could do this for all all square numbers.
    
    if(i>=7):
        d=-1
    elif(i<=2):
        d=1

    i+=d

    time.sleep(.5)# sleep is here to allow the output to be readable