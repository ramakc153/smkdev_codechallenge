import time
number = input("input the number : ")
start = time.time()
while int(number) != 1:
    temp_sum = 0
    if time.time() - start >=5:
        print("code exit after 5 seconds ")
        break
    for num in range(len(number)):
        # print("ini num", num)
        temp_sum += int(number[num]) ** 2
    number = str(temp_sum)
    print("ini number ", number)

print(number)