# Example hardcoded weight for testing
weight = 5.0  

# Initialize variables for shipping costs
cost_ground = 0.0
cost_ground_premium = 125.00  # Fixed cost for premium ground shipping
cost_drone = 0.0

# Ground Shipping Cost Calculation
# Determine the price per pound based on weight
if weight <= 2:
    price_per_pound = 1.50
elif weight <= 6:  # Corrected condition to check weight range
    price_per_pound = 3.00
elif weight <= 10:  # Corrected condition to check weight range
    price_per_pound = 4.00
else:  # For weights over 10 lbs
    price_per_pound = 4.75

# Calculate total cost for ground shipping
cost_ground = weight * price_per_pound + 20.00  # Adding a base fee of $20.00
print("Ground Shipping Cost: $", cost_ground)

# Ground Shipping Premium Cost
print("Ground Shipping Premium Cost: $", cost_ground_premium)

# Drone Shipping Cost Calculation
# Determine the price per pound based on weight for drone shipping
if weight <= 2:
    price_per_pound_drone = 4.50
elif weight <= 6:  # Corrected condition to check weight range
    price_per_pound_drone = 9.00
elif weight <= 10:  # Corrected condition to check weight range
    price_per_pound_drone = 12.00
else:  # For weights over 10 lbs
    price_per_pound_drone = 14.25

# Calculate total cost for drone shipping
cost_drone = weight * price_per_pound_drone
print("Drone Shipping Cost: $", cost_drone)

# Determine the cheapest shipping method
if cost_ground < cost_ground_premium and cost_ground < cost_drone:
    print('Ground shipping is cheapest: $', cost_ground)
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
    print('Ground shipping premium is cheapest: $', cost_ground_premium)
else:
    print('Drone shipping is cheapest: $', cost_drone)





##### Sample https://github.com/Codecademy/learn-python/blob/main/2-control-flow/sals-shipping/shipping.py
