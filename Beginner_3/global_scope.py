enemies = 1

#Not the prefer way
"""
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")
"""    
 
# Do this instead

def increase_enemies(enemy):
    print(f"Enemies inside function: {enemies}")
    return enemy + 1
    
enemies = increase_enemies(enemies)    

print(enemies) 