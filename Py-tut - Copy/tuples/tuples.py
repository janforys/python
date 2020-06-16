# Tuples are invariable.
coordinates = (14.3599, 67.015)
print(coordinates[1])

# Variable "coordinates2" is a list of tuples.
coordinates2 = [coordinates, (0.21, -0.21), (99.995, 789.0023)]
print(coordinates2)
coordinates2.insert(0, (1, 1))
print(coordinates2)
