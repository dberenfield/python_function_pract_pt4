
def max_num(x, y, z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
    return largest

    print(max_num)


    mult_list=[3,4,5,4,7]
total = 1
for i in mult_list:
	total *= i

print(total)


def rev_string(s):
    str = ""
    for i in s:
        str = i + str
    return str

    

def num_within(n):
    if n in range(3, 9):
        print("The number is in the range" % str(n))
    else:
        print("The number is outside the given range.")
