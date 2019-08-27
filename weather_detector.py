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