gravity = [3.7, 8.87, 9.8, 3.71, 24.79, 10.44, 8.87, 11.15]
H = float(input("Initial height (m): "))  # Asks the user for the initial height
g = int(input("Select the planet your object is at:\n "
              "1. Mercury\n 2. Venus\n 3. Earth\n 4. Mars\n 5. Jupiter\n "
              "6. Saturn\n 7. Uranus\n 8. Neptune\n")) - 1  # Subtract 1 to match the list index
T = (2 * H / gravity[g]) ** 0.5  # Total fall time (float)
T2 = int(T // 1)  # Total fall time (integer)
t = 0  # t is defined as a time during the fall

for t in range(T2):
    y = H - 0.5 * gravity[g] * t ** 2  # Position function
    print("At t =", t, " s the height is", y, " m")
    t += 1

y = H - 0.5 * gravity[g] * T ** 2
print("At t =", T, " s the height is", y, " m")
