#dictdemo.py

candies = {}

candies['snickers'] = 8.5
candies['milky way'] = 7.5
candies['black licorice'] = 1.0
candies["reese's cup"] = 10.0
candies['bit-o-honey'] = 11.0

print(len(candies))
print(candies)
print(candies['snickers'])

for rating in candies.values():
    print(rating)
