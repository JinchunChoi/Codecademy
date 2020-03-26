def cost_ground_shipping(weight):
  flat_charge = 20
  cost = 0
  ppp = 0.0
  if weight < 2:
    ppp = 1.5
  elif 2 < weight <= 6:
    ppp = 3.0
  elif 6 < weight <= 10:
    ppp = 4.0
  else:
    ppp = 4.75    
  cost = weight * ppp + flat_charge
  return cost

print(cost_ground_shipping(8.4))

premium_ground_shipping = 125

def cost_drone_shipping(weight):
  flat_charge = 0
  cost = 0
  ppp = 0.0
  if weight < 2:
    ppp = 4.5
  elif 2 < weight <= 6:
    ppp = 9.0
  elif 6 < weight <= 10:
    ppp = 12.0
  else:
    ppp = 14.75
  cost = weight * ppp + flat_charge
  return cost    
print(cost_drone_shipping(1.5))


def cost_shipping(weight):
  ground = cost_ground_shipping(weight)
  drone = cost_drone_shipping(weight)
  premium = premium_ground_shipping
  
  if ground < drone and ground < premium:
    print("use ground")
    return ground
  elif drone < ground and drone < premium:
    print("use drone")
    return drone
  elif premium < ground and premium < drone:
    print("use premium")
    return premium

print(cost_shipping(4.8))
print(cost_shipping(41.5))
print(cost_shipping(17))
