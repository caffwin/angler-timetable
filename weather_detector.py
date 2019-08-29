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

    print("Window to match is: " + window_string)

    # Loop through each 
    for i in range(0, len_list - 1):
        # print("Entered for loop!")
        # Create new list to hold test window
        # Append first element, list[i], to test_window
        # Append second element, list[i+1], to test_window
        test_window = []
        test_window.append(weather_list[i][0])
        # print("Weather_list at index...", weather_list[i])
        test_window.append(weather_list[i + 1][0])
        print("Test window is: ", test_window)
        # Check if they are equal

        if test_window == match_this_window:
            print("Window match found! " + window_string)
            print("Window time begins at (in-game time): " + weather_list[i][1])

    return 
    # Continue going through the entire list - the test window may occur more than once


    # If the slider window matches the current window, print out a notification and continue
    # traversing until the end of the list





# find_weather_pattern(["Clouds", "Fair Skies", "Clear", "Clear", "Thunder", "Clear", "Fair Skies", "Fog"], "Thunder", "Clear")


w1 = ("Clouds", "00:00")
w2 = ("Fair Skies", "08:00")
w3 = ("Clear", "16:00")
w4 = ("Clear", "00:00")
w5 = ("Thunder", "8:00")
w6 = ("Clear", "16:00")
w7 = ("Fair Skies", "00:00")
w8 = ("Fog", "8:00")

weather_time_list = [w1, w2, w3, w4, w5, w6, w7, w8]
print("Weather time list is: ", weather_time_list)
print(weather_time_list[0][0])


print("Second try: ")
find_weather_pattern(weather_time_list, "Thunder", "Clear")


# Next step: change list elements into tuples instead of strings, so that each weather condition also 
# includes the time (in game time) when the weather change occurs



# Eventually: 
# Figure out how to pass in-game time and weather patterns from client-side to server