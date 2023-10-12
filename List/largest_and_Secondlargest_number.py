#Find the largest and second largest value of the 5 numbers entered by user without using list

max = float('-inf') #Initiate a number as negative infinity
i=0
while(i<5): #Code is considered for 5 random integers entered by user. (+ve or negative)
    x = int(input("Enter a Number: "))
    if(max<x):
        second_max = max #First Assign the value of -infinity to second max
        max=x #Assign the value of x to max
    elif(x>second_max):
        second_max = x
    i=i+1
print("Max is: ",max)
print("Second Max: ", second_max)