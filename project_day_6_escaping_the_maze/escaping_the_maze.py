#unfinished reeborg's world project
# i'll be right back after a week

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while front_is_clear():
    move()  
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()    
    elif front_is_clear():
        move()
    else:
        turn_left()