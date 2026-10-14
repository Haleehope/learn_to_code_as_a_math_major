# ###################################################################
# Find the mountain peaks
# ###################################################################

# create a function that returns a dictionary of the index and elevation in the dataset list where there's a peak
def find_peaks(data):
    # initialize the dictionary (create an empty dictionary)
    peaks = {}

    # for each index in the elevations list, if the element in the list is greater than both its neighbors, add it to the dictionary
    for i in range(1, len(data) - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peaks[i] = data[i]

    # return the dictionary
    return peaks

# create a list of the given elevations from the dataset
elevations = [2, 5, 3, 7, 4, 8, 6]

# call the function to find the peaks
peaks = find_peaks(elevations)

# print the mountain peaks by printing the (key, value) pairs in the dictionary
print("Mountain peaks:")
for index, elevation in peaks:
    print(f"Position {index}: elevation {elevation}")
