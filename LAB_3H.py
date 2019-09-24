lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]
#
print(friends)
print(lucky_numbers)
#
friends.extend(lucky_numbers)
print(friends)
#
print("\n ------------------ ")
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]
#
friends.append("Olek")
print(friends)
#
friends.insert(1, "Aleksander")
print(friends)
#
friends.remove("Olek")
print(friends)
#
friends.clear()
print(friends)
#
print("\n ------------------ ")
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]
#
friends.pop()
print(friends)
print(friends.index("Jane"))
print(friends.count("Jim"))
friends.sort()
lucky_numbers.sort()
friends.reverse()
lucky_numbers.reverse()
#
friends2 = friends.copy()
print(friends2)
#
coordinates = (4, 5)
print(coordinates)
print(coordinates[0])