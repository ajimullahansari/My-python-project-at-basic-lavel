num = int(input("enter a number here:"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit **3
    temp //=10
if sum == num:
    print("it is a armstrong number:")
else:
    print("not a armstronge number:")