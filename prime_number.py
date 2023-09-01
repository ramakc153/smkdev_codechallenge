import time
lower = int(input("masukkan angka lower :"))
upper = int(input("masukkan angka upper :"))
is_prime = 0
total_prime_number =0
start = time.time()
for current_number in range(lower, upper+1):
    for divider in range(2,int(current_number/2)+1):
        if current_number % divider == 0 :
            is_prime+= 1
            break
    if is_prime == 0:
        print(str(current_number) + 'is rill prime')
        total_prime_number += 1
    else : 
        print(str(current_number) + "you're not prime")
    is_prime = 0

print('total prime number in interval are : ', total_prime_number)
end = time.time()

print("execution time : ", end-start)