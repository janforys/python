numbers = [34, 43, 2, 1, 99]
cities = ["Gdańsk", "Warszawa", "Wrocław", "Białystok"]

print(numbers, cities)
print(numbers)
print(cities)

numbers.reverse()
print(numbers)

numbers.extend(cities)
cities.extend(numbers)
print(numbers)
# Note that "numbers" list is already extended.
print(cities)

cities.append("Poznań")
print(cities)
numbers.insert(2, 666)
print(numbers)

numbers.clear()
print(numbers)
print(cities.index("Warszawa"))
numbers.reverse()
print(numbers)