enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")
    
increase_enemies()
print(f"Enemies outside function: {enemies}")    

# Local Scope
def drink_potion():
    potion_strenght = 2
    print(potion_strenght)
    
drink_potion()
#print(potion_strenght)    # Will give an error NameError: name 'potion_strenght' is not defined


# Global Scope
player_healt = 10 # Global variable

def drink_potion_2():
    potion_strenght_2 = 3 # Local variable
    print(player_healt)
    
drink_potion_2()    