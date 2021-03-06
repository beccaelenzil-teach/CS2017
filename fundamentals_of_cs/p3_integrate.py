import math

x_frac = 0
frac_list = []
x_list = []
y_list = []
low = 2
hi = 10
N = 10
area = 0
x = low

def f(x):
    return 2*x

for i in range(N):
    x += (1/N)*(hi-low)
    x_list.append(x)

print(x_list)

for x in x_list:
    y_list.append(f(x))

x_diff = x_list[1] - x_list[0]

for y in y_list:
    area += x_diff*y

print(area)




def dbl(x):
  """ input: a number x (int or float)
    output: twice the input
  """
  return 2*x

def unitfracs(N):
    frac = 0
    frac_list = []
    for i in range(0,N):
        frac_list.append(frac)
        frac += 1/N

    return frac_list

#print(unitfracs(4))

def scaledfracs(low,hi,N):
    scaled_list = []
    frac_list = unitfracs(N)
    for frac in frac_list:
        scaled_list.append(low+frac*(hi-low))
    return scaled_list

#print(scaledfracs(10, 30, 5 ))

def sqfracs(low,hi,N):
    sqfracs_list = []
    scaled_list = scaledfracs(low,hi,N)
    for frac in scaled_list:
        sqfracs_list.append(frac**2)

    return sqfracs_list

#print(sqfracs(4,10,6))

def f_of_fracs(f,low,hi,N):
    y_list = []
    scaled_list = scaledfracs(low,hi,N)
    for frac in scaled_list:
        y_list.append(f(frac))

    return y_list

#print(f_of_fracs(math.sin, 0, math.pi, 4))

def integrate(f,low,hi,N):
    total = 0
    y_list = f_of_fracs(f,low,hi,N)
    x_list = scaledfracs(low,hi,N)
    x_diff = x_list[1]-x_list[0]
    for i in range(len(y_list)):
        total += y_list[i]*x_diff

    return total

#print(integrate(math.sin, 0, math.pi, 1000))
