while True:
    # 
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        move(West)
        if i == get_world_size() - 2:
            if can_harvest():
                harvest()
            move(North)    
            break
    # bucle para bush
    for i in range(get_world_size()):
        if i == get_world_size() - 4:
            if can_harvest():
                harvest()
                plant(Entities.Bush) 
            move(East)
            if can_harvest():
                harvest()
                plant(Entities.Tree)
            move(North)    
            break
        if can_harvest() or get_entity_type() == None:
            harvest()
            plant(Entities.Bush)
        move(East)
        if can_harvest() or get_entity_type() == None:
            harvest()
            plant(Entities.Tree)
        move(East)

            
    for i in range(get_world_size()):
        if get_ground_type() != Grounds.Soil:                
            till()
        if get_entity_type() == None:
            plant(Entities.Carrot)
        if can_harvest():    
            harvest()
            plant(Entities.Carrot)
        move(West)
        if i == get_world_size() - 2:
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() == None:
                plant(Entities.Carrot)
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
            move(North)
            move(West)
            break