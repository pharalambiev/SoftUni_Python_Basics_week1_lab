length = int(input())
width = int(input())
hight = int(input())
occupied_percentage = float(input())

tank_capacity = length*width*hight
liters_total = tank_capacity/1000
liters = (liters_total*occupied_percentage)/100

water = liters_total - liters

print (water)