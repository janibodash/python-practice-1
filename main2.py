
driver = str(input("Enter driver name: "))
destination = input("Enter destination:  ")
distance = float(input("Enter  distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (KZT/L): "))


litres_needed = distance * consumption / 100
fuel_cost = litres_needed * price
cost_per_km = fuel_cost / distance

if distance < 100:
    category = "Short trip"
elif distance>=100 and distance<500:
    category = "Medium trip"
elif distance>=500:
    category = "Long trip"

print("="*30)

print("Driver : ",driver)
print("Destination : ",destination.upper())
print("Distance : ", distance ,"km")
print("Fuel cost : ", fuel_cost)
print("Category : ", category)

print("="*30)

print("Cost breakdown:")

for i in range(100,int(distance) + 1,100):
    cost_so_far = (i / 100) * consumption * price
    print(i, "km ->", cost_so_far, "KZT")



print("Destination analysis:")
print("Uppercase :", destination.upper())
print("Lowercase :", destination.lower())
print("Length :", len(destination))
print("Letter 'a' count :", destination.lower().count('a'))