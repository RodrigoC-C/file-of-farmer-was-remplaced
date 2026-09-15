def ciclo_riego():
    if get_water() <= 0.75:
        use_item(Items.Water)
    return None

def ciclo_fertilizante():
    return None
    