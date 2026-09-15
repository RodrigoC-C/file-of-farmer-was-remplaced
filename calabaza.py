from potenciadores import ciclo_riego
while True:
    # 
    for i in range(get_world_size()):
        if i == 0 or i == 1:
            if can_harvest() or get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
                if get_ground_type() != Grounds.Soil:
                    till()
                harvest()
                ciclo_riego()
                plant(Entities.Pumpkin) 
            move(East)
        if can_harvest() and i >= 2:
            harvest()
            ciclo_riego()
            move(East)
        if i == get_world_size() - 2:
            if can_harvest():
                harvest()
                ciclo_riego()
            move(North)    
            break
            
    # bucle para bush
    for i in range(get_world_size()):
        if i == get_world_size() - 4:
            if can_harvest() or get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
                if get_ground_type() != Grounds.Soil:
                    till()
                harvest()
                ciclo_riego()
                plant(Entities.Pumpkin) 
            move(West)
            if can_harvest() or get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
                if get_ground_type() != Grounds.Soil:
                    till()
                harvest()
                ciclo_riego()
                plant(Entities.Pumpkin)
            move(North)    
            break
        if can_harvest() or get_entity_type() == None:
            harvest()
            ciclo_riego()
            plant(Entities.Bush)
        move(West)
        if can_harvest() or get_entity_type() == None:
            harvest()
            ciclo_riego()
            plant(Entities.Tree)
        move(West)

            
    for i in range(get_world_size()):
        if get_ground_type() != Grounds.Soil:                
            till()
        if get_entity_type() == None:
            plant(Entities.Carrot)
            ciclo_riego()
        if can_harvest():    
            harvest()
            plant(Entities.Carrot)
            ciclo_riego()
        move(East)
        if i == get_world_size() - 2:
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() == None:
                plant(Entities.Carrot)
                ciclo_riego()
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
                ciclo_riego()
            move(North)
            move(East)
            break