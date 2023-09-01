import time  # this library is not necessary, just to count how long the execution time
lower = int(input("masukkan angka lower :")) #lower interval number 
upper = int(input("masukkan angka upper :"))  #upper interval number
isNot_prime = 0  #flag to check whether the number is prime or not
prime_numbers = []  # array that contain list of prime number
# total_prime_number =0
start = time.time()   
for current_number in range(lower, upper+1):  #loop from lower interval to upper interval (+1 is used to include the upper interval)
    for divider in range(2,int(current_number/2)+1):  #loop for dividing current number with the divider from 2 to current number
        if current_number % divider == 0 :  #to check the current number is divisible by divider number
            isNot_prime+= 1   # add flag to 1 if number is divisible by divider (marked as not prime number)
            break  # no need to check until the last loop, so break from loop
    if isNot_prime == 0:   
        # print(str(current_number) + 'is rill prime')  #debug purpose
        prime_numbers.append(current_number) #if the number is prime, it will added to array
    # else : 
    #     print(str(current_number) + "you're not prime")  #debug purpose
    isNot_prime = 0  # set flag to 0 again for the next number that we want to check

print(f"list of prime number : [{', '.join(map(str,prime_numbers))}]")  #print list of prime number
print('total prime number in interval are : ', len(prime_numbers))   #print how many prime number(s) in interval
end = time.time()

print("execution time : ", end-start)