# ###################################################################
# Earthquake magnitude comparison
# ###################################################################

# the def keyword denotes the beginning of a function in Python
# a function in code is exactly like a function in math
# say our function is: f(x) = 2x if x > 4 and 3x if x <=4
# we could write this as
# def f(x):
#   if x > 4:
#       return 2*x
#   else: 
#       return 3*x


# usually, you create functions when you want to reuse the same code without having to rewrite it every time
# for example, your boss says you need to compute f(x) for 3, 4, and 5 as inputs
# instead of writing 2*3, 2*4, and 3*5, we would write f(3), f(4), and f(5)
# later, your boss says that f(x) is actually 2x if x > 6 and 3x otherwise
# if you had originally written 2*3, 2*4, and 3*5, you would need to change all those instances in the code
# instead, if you just called the function in your code: f(3), f(4), and f(5), you can just change the function to
# def f(x):
#   if x > 6:
#       return 2*x
#   else: 
#       return 3*x
# and everything else will still work

# NOTE: functions are written at the top of each file under imports as a good coding convention since it's easier to find and edit them if they are all near the top

# create a function that will take in two seismic wave amplitudes, say A_1 and A_2, and will return 10^{A_1-A_2}
def amplitude_ratio(m1, m2):
    return 10 ** (m2 - m1)

# create a function that will take in two seismic wave amplitudes, say A_1 and A_2, and will return 10^{A_1-A_2}
def amplitude_ratio_bonus(m1, m2):
    return 10 ** (1.5*(m2 - m1))

# take in two inputs: the mangitudes of the first and second earthquake
# convert them to floats since the user should have made them numeric
m1 = float(input("First earthquake magnitude: "))
m2 = float(input("Second earthquake magnitude: "))

# call your handy dandy function and store the result in a variable called 'ratio'
ratio = amplitude_ratio(m1, m2)

# now print out the outputs
# I used a format for printing called f-print which is where the f is for formatted strings
# using f-print, I can format the ratio with :2f, which just formats the floats to print out only two decimal places
if m2 > m1:
    print(f"The second earthquake has {ratio:.2f} times the amplitude.")
elif m1 > m2:
    print(f"The first earthquake has {1 / ratio:.2f} times the amplitude.")
else:
    print("Both earthquakes have the same magnitude.")
