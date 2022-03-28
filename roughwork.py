def sum_all(*args):
    sum = 0

    for num in args:
        if not str(num).isdigit():
            print("Error")
        else:
            sum += int(num)
    print(sum)
sum_all(1,2,3,4,"t")
