print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

way = input('Please select your way. "left" or "right": \n')
if way == "left":
    action = input('You\'ve come to a lake. '
                   'There is an island in the middle of the lake. '
                   'Type wait to wait for a boat. '
                   'Type swim to swim accross. \n').lower()
    if action == "wait":
        door_color = input('You arrived at the island unharmed. '
                           'There is a house with 3 doors. One red, '
                           'one yellow and one blue. '
                           'Which colour do you choose? \n').lower()
        if door_color == "yellow":
            print("You found the treasure. You Win!")
        elif door_color == "red":
            print("It's a room full of fire. Game Over! ")    
        elif door_color == "blue":
            print("You entered a room of beast. Game Over.")
        else:
            print("You chose a door that does not exist. ")        
    else:
        print("You got attacked by an angry trout. Game Over.")    
else: 
    print("You fell into a hole. Game Over!")    

