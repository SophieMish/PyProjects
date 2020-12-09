max = 1
counter_Max = 0


for i in range(1, 1000):
    num_Now = i
    counter = 0
    while num_Now != 1:
        if num_Now % 2 == 1:
            num_Now = 3 * num_Now + 1
        else:
            num_Now = num_Now/2
        counter += 1
    if counter > counter_Max:
        max = i
        counter_Max = counter
print("Максимальное число:",max,"\nКоличество итераций:",counter_Max)