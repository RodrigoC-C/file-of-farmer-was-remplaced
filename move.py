def move_exact(x, y):
    x_now = get_pos_x()
    y_now = get_pos_y()
    
    if get_world_size() <= x or get_world_size() <= y:
        alert = quick_print("El numero no puede sobrepasar el tamñano del mundo = ", get_world_size())
        return alert
    
    quick_print(x_now, y_now)
    #North 1
    #South -1
    #East 1
    #West -1
    move_x = x - x_now
    move_y = y - y_now
    # quiero moverme a la posicion 2,3. estoy en la posicion 7,8 

    if move_x > 0:
        for i in range(move_x):
            move(East)
        
    if move_x < 0:
        for i in range(move_x * -1):
            move(West)
        
    if move_y > 0:
        for i in range(move_y):
            move(North)
        
    if move_y < 0:
        for i in range(move_y* -1):
            move(South)
        
