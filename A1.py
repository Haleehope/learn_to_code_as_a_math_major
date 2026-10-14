# ###################################################################
# How far to the center of the Earth?
# ###################################################################

# the earth's radius in kilometers to be 6,371
EARTH_RADIUS_KM = 6371

# we will prompt the user for their depth and then ask them if that depth is in kilometers or miles
# we can make (aka "cast") the depth as a float because the user should've inputted a numerical value
# these inputs will show up in the 
depth = float(input("Enter depth: "))
unit = input("Is that in km or miles? ").lower()

# if they said miles, we convert that depth to kilometers to get it to be the same units as our googled radius
if unit == "miles":
    depth = depth * 1.60934

# subtract the depth from the radius
distance = EARTH_RADIUS_KM - depth

# now we can do some error handling
# error handling is when you handle potential errors
# for example, the user could put a depth greater than the distance to the center of the earth
# or they could put a negative depth
# so, we can catch those errors in an if statement to print out an appropriate response
if 0 <= depth <= EARTH_RADIUS_KM:
    print(f"Distance to Earth's center: {distance:.2f} km")
else:
    print("That depth is outside the valid range.")
