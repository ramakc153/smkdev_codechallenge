# code advantage : able to check multiple missing number
n_number  = int(input("Input n range number : "))  #accept input for range number from user
a = list(range(1,n_number+1))  #create sequence of number from 1 to n_number
b = input("Input sequence number: ").split(" ")  #accept sequence number input from user
b = list(map(int,b))  #doesn't really necessary line. just converting str to int element

missing = []  #variable to store missing number
#this looping is check whether sequence of number inputter by user is missing or not
for number in a:  
    if number not in b: #if number doesn't exist from input user, add to missing number array
        missing.append(number)
print("missing number are: ",missing) #print missing number