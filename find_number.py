'''Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700'''

def find_num(l_limit,u_limit):
    num = []
    for i in range(l_limit,u_limit):
        if i % 7 == 0 and i % 5 ==0:
            num.append(i)
    print(num)

if __name__ == "__main__":
    l_limit = int(input("Enter the lower limit:"))
    u_limit = int(input("Enter the upper limit:"))
    find_num(l_limit,u_limit)

