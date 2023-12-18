
def max_num(x, y, z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
    return largest

    print(max_num)


  def mult_list(num):
a = 1
for i in num:
	a = a * 1
    return a
    print(mul[5,2,3])

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



def pascal(n):
    trow = [1]
     y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
      return n >= 1
pascal(6) 