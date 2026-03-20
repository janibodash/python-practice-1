driver = str(input("Driver : "))
distance = float(input("Distance : "))
consumption = float(input("Consumption : "))
price = float(input("Fuel price : "))

litres_needed = distance * consumption / 100
fuel_cost = litres_needed * price
cost_per_km = fuel_cost / distance

print("="*30)
print("      ROAD TRIP SUMMARY     ")
print("="*30)


print("Driver : ",driver)
print("Distance : ", distance ,"km")
print("Consumption : ", consumption, "L/100km")
print("Fuel price : ", price, "KZT/L")

print("-"*30)

print("litres needed: ",litres_needed, "L")
print("fuel cost: ",fuel_cost, "KZT")
print("cost per km: ",cost_per_km, "KZT")

print("="*30)

print("Trip longer than 300 km: ", distance > 300)
print("Fuel cost above 5000 KZT: ",  fuel_cost> 5000)