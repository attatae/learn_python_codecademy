weight_lb = int(input("Item Weight (Lbs):"))#in pounds 
#price_per_lb = 0
total_price_ground = 0.00
#print("Item weight: ", weight_lb)
cost_premium_gr_ship = 125
total_price_drone = 0.00

#Ground Shipping
if weight_lb <= 2:
  total_price_ground = weight_lb * 1.50 + 20
elif 6 >= weight_lb > 2:
  total_price_ground = weight_lb * 3.00 + 20
elif 10 >= weight_lb > 6:
  total_price_ground = weight_lb * 4.00 + 20
elif weight_lb > 10:
  total_price_ground = weight_lb * 4.75 + 20
  
# drone shipping 
if weight_lb <= 2:
  total_price_drone = weight_lb * 4.50
elif 6 >= weight_lb > 2:
  total_price_drone = weight_lb * 9.00
elif 10 >= weight_lb > 6:
  total_price_drone = weight_lb * 12.00
elif weight_lb > 10:
  total_price_drone = weight_lb * 14.25
  
if (total_price_ground or total_price_drone) > 125:
  print("For this order we recommend our Premium Ground Shipping Service for only $125. Otherwise the price is: ")
  
print("Ground Shipping: $" + str(total_price_ground))
print("Drone Shipping: $" + str(total_price_drone))

