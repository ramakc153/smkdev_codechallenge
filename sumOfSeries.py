number = input("input number : ")
multiply = int(input("input how much number to multiply : "))

array = []

for times in range(1,multiply):
    array.append(number*times)
array = list(map(int,array))
print(sum(array))