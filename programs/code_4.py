# closed - True Opened - False

window_one = False 
window_two = False 

front_door = False 
back_door = False 

if window_one and window_two:
    print("Windows Are Closed.")
else:
    print("Windows Are Not Closed.")

if front_door or back_door:
    print("House Is Accessible.")
else: 
    print("House Is Not Accessible.")

if not front_door or not back_door:
    print("Check Doors.")
