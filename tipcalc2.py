# this version tip calculator ensures only numbers can be input
# it will keep asking the user for correct inputs until provided
# this program does not allow the user to enter negitive numbers


# ask user bill amount and tiptry
while True:
    try:
        BA = int(input("How much is your bill?"))
        TR = int(input("% You would like to tip?"))
        break
    except ValueError:
        print("Enter numerical value.")
# convert string to float
Float = float(BA)
Floaty = float(TR)
#calculate tips and the total
tip = Float * (Floaty / 100)
total = Float + tip
# dont allow for negitive numbers to be input by the user
# round out the values and display
if tip > 0:
    print("tip: $", (round(tip, 2)))
    print("total: $", (round(total, 2)))
else:
    print("No negitive inputs please.")
