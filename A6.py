# ###################################################################
# Earthquake logbook
# ###################################################################

# start with writing a list of these magnitudes
magnitudes = [2.1, 4.5, 3.2, 5.8, 1.9, 4.0]

# print the largest, smallest, and average magnitude
print("Largest:", max(magnitudes))
print("Smallest:", min(magnitudes))
print("Average:", sum(magnitudes) / len(magnitudes))

# write a function that returns a list of earthquakes above a given magnitude threshold
def earthquakes_above(data, threshold):
    results = []

    # for each magnitude in a list of magnitudes from the dataset
    # if the magnitude is greater than a threshold, add that magnitude to the list
    for magnitude in data:
        if magnitude > threshold:
            results.append(magnitude)

    # NOTE: I gave you the magnitudes in the dataset, so you could have hard coded that into this function instead of making it a parameter
    # but if you needed to run this code for multiple different dataset magnitudes, then it's good that you didn't hard code the original dataset
    # this is called "generalizing your code", and it's good code convention because it makes it easier to make edits later
    return results

# get the threshold from the user
threshold = float(input("Enter magnitude threshold: "))

# print the earthquakes above the threshold
print("Earthquakes above threshold:\n", earthquakes_above(magnitudes, threshold))
