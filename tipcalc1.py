
# ask user bill amount and tip
BA = input("How much is your bill?")
TR = input("% You would like to tip?")
# convert string to float
Float = float(BA)
Floaty = float(TR)
#calculate tips + total
tip = Float * (Floaty / 100)
total = Float + tip
# round out the values + display
print("tip: $", (round(tip, 2)))
print("total: $", (round(total, 2)))
