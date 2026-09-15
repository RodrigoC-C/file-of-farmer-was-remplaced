while True:

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        move(West)
        if i == get_world_size() - 2:
            if can_harvest():
                harvest()
            move(North)    
            break

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(Entities.Bush)
        move(East)
        if i == get_world_size() - 2:
            if can_harvest():
                harvest()
                plant(Entities.Bush)
            move(North)    
            break

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
            