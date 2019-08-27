# Objective: To check any two consecutive weather patterns in a given array, and return True
# if a specific pattern comes up

# Example: 
# The next eight weather patterns are ["Clouds", "Fair Skies", "Clear", "Clear", "Thunder", "Clear", "Fair Skies", "Fog"]
# The weather pattern to look for is "Thunder" > "Clear"
# The input will include the list of weather patterns for the next eight windows, the first required
# weather condition and the second required weather condition as separate arguments
# Testfor negative: Check for "Thunder" > "Fog"

# def find_weather_pattern(weather_lst, first, second)

# Output: "True" if first and second required conditions appear consecutively, and "False" otherwise


# Approach:
# Basic window slider algorithm

# Notes:
# First and second can be equal to eachother, the same weather


def find_weather_pattern(weather_list, first, second):

    # Initialize sequence to check
    len_list = len(weather_list)
    match_this_window = [first, second]
    window_string = match_this_window[0] + " > " + match_this_window[1]

    print("Window to match is: ", window_string)

    # Loop through each 
    for i in range(0, len_list - 1):
        # Create new list to hold test window
        # Append first element, list[i], to test_window
        # Append second element, list[i+1], to test_window
        test_window = []
        test_window.append(weather_list[i])
        test_window.append(weather_list[i + 1])

        # Check if they are equal
        if test_window == match_this_window:
            print("Window match found! " + window_string)

    return 
    # Continue going through the entire list - the test window may occur more than once


    # If the slider window matches the current window, print out a notification and continue
    # traversing until the end of the list





find_weather_pattern(["Clouds", "Fair Skies", "Clear", "Clear", "Thunder", "Clear", "Fair Skies", "Fog"], "Thunder", "Clear")


# Next step: change list elements into tuples instead of strings, so that each weather condition also 
# includes the time (in game time) when the weather change occurs



# Eventually: 
# Figure out how to pass in-game time and weather patterns from client-side to server