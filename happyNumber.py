import time
number = input("input the number : ")  #Input number to check
start = time.time()  #variable for timeout 
while int(number) != 1:  #create while loop while the result number not equal to 1
    temp_sum = 0  #temp variable to assign to current number
    # This logic will triger if code run more than 5 seconds
    if time.time() - start >=5:
        print("code exit after 5 seconds ")
        break
    for num in range(len(number)):
        # print("ini num", num)
        temp_sum += int(number[num]) ** 2  #sum of square number of each digit
    number = str(temp_sum)  #assigning the number variable
    print("ini number ", number)

print(number)