# ###################################################################
# Earthquake countdown
# ###################################################################

# import the math library to use math.ceil which rounds a float up to the nearest integer (the opposite of math.floor)
import math

# an imaginary seismic wave is predicted to travel either 5 km/s and 3 km/s
FAST_WAVE_SPEED = 5   # km/s
SLOW_WAVE_SPEED = 3   # km/s

# prompt the user for the distance to an earthquake
distance = float(input("Distance to earthquake (in km): "))

# error handle if the distance the user gave is nonpositive
if distance < 0:
    print("Distance must be nonnegative.")

else:
    fast_time = distance / FAST_WAVE_SPEED
    slow_time = distance / SLOW_WAVE_SPEED

    # print the seconds until the fast and slow wave arrive
    # dimenions: T = L / (L/T)
    print(f"Fast wave arrives in {fast_time:.1f} seconds.")
    print(f"Slow wave arrives in {slow_time:.1f} seconds.")

    # print the time between the slow and fast waves
    print(f"Time between waves: {slow_time - fast_time:.1f} seconds")

    # use a for loop to print the seconds until the earthquake occurs 
    # these print statements will occur much faster than 1 second, but this is just a cute little assignment
    # range takes in three input parameters: the first number, the last number, and how to step across that range
    # having -1 as the third parameter means that it increments by -1 (effectively reversing to create a countdown instead of counting up)
    for seconds in range(math.ceil(fast_time), 0, -1):
        print(seconds)

    # print that the fast wave arrived 
    print("Fast wave has arrived!")