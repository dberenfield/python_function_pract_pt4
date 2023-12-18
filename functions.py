
def max_num(x, y, z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
    return largest

    print(max_num)


def mult_list(lst):
  if len(lst) == 0:
    return 0
  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i
  return prod

print(mult_list([6,7,3]))


def rev_string(s):
    str = ""
    for i in s:
        str = i + str
    return str

    

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(2,6,8))     
print(num_within(2,1,3))

def pascal(n):
    trow = [1]
y = [0]
for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
return n >= 1
pascal(6) 