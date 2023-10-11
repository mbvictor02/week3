#Definition of a function that calculates the area of a circle with the value of its radius
def area(radius):
    return float(3.1416*radius**2)

#Asks user the lenght of the radius and stores it in a float variable
radius_input = float(input("Type in the radius lenght of the circle (in m): "))
#Calculates area of the cirlce using the previously defined function and prints it   
print(f"The area of the circle  is {area(radius_input)} square meters")