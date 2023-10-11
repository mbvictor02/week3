H = float(input("Initial height:  "))               #Asks user the inital height
g = float(input("Select the planet your object is at:\n" "Mercurio"))
T = (2*H/g)**1/2                                    #Total fall time (float)
T2 =int( T//1)                                      #Total fall time (integrer)
t = float(0)                                        #t is defined as a time during the fall   


for t in range (T2):
    y = H-1/2*g*t**2                                #Position function 
    print ("At t = ", t, " the height is ", y)
    t += 1

y = H-1/2*g*T**2
print ("At t = ", T, " the height is ", y)

Mercurio	3,7 m/s²
Venus	8,87 m/s²
La Tierra	9, 8 m/s²
Marte	3,71 m/s²
Júpiter	24,79 m/s²
Saturno	10,44 m/s²
Urano	8,87 m/s²
Neptuno	11,15 m/s²