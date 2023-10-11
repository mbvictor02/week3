import random

def montecarlo(total_points):  # This function will estimate pi once
    points_in = 0  # points_in initialized to 0 for the next iteration

    for i in range(total_points):
        x = random.uniform(0, 1)  # Making use of the random library, both x and y coordinates
        y = random.uniform(0, 1)  # of one point per iteration are generated randomly

        # The magnitude of the vector with coordinates (x, y), considering that the
        # grid center is the center of the circle, is calculated
        magnitude = x ** 2 + y ** 2

        # Hence, if the magnitude is smaller than the radius (1), the point generated on a given
        # iteration will be inside the circle, so we add 1 to the variable "points_in"
        if magnitude <= 1:
            points_in += 1

    return 4 * points_in / total_points  # Returns estimated value of pi

# Asks for user inputs
total_points = int(input("Total number of points to generate: "))
tries = int(input("Number of times you want to run the method: "))
# Definition of a list that will include "tries" estimated values of pi
pi_values = []

for j in range(tries):
    # pi_values is filled by calling montecarlo "tries" times
    pi_values.append(montecarlo(total_points))

# Calculate the average of all pi values and the standard deviation
estimated_pi = sum(pi_values) / tries
standard_deviation = (sum((x - estimated_pi) ** 2 for x in pi_values) / tries) ** 0.5

# Print the result
print(f"The estimated value of pi is: {estimated_pi} +/- {standard_deviation}")
