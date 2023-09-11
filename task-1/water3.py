def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4



def successors(s):
    x, y, z = s
    actions = []

    # Pour water from the 8-liter bottle to the 5-liter bottle
    if x > 0 and y < 5:
        pour_amount = min(x, 5 - y)
        new_state = (x - pour_amount, y + pour_amount, z)
        actions.append((new_state, pour_amount))
    # Pour water from the 8-liter bottle to the 3-liter bottle
    if x > 0 and z < 3:
        pour_amount = min(x, 3 - z)
        new_state = (x - pour_amount, y, z + pour_amount)
        actions.append((new_state, pour_amount))
    # Pour water from the 5-liter bottle to the 3-liter bottle
    if y > 0 and z < 3:
        pour_amount = min(y, 3 - z)
        new_state = (x, y - pour_amount, z + pour_amount)
        actions.append((new_state, pour_amount))
    # Pour water from the 5-liter bottle to the 8-liter bottle
    if y > 0 and x < 8:
        pour_amount = min(y, 8 - x)
        new_state = (x + pour_amount, y - pour_amount, z)
        actions.append((new_state, pour_amount))
    # Pour water from the 3-liter bottle to the 5-liter bottle
    if z > 0 and y < 5:
        pour_amount = min(z, 5 - y)
        new_state = (x, y + pour_amount, z - pour_amount)
        actions.append((new_state, pour_amount))
    # Pour water from the 3-liter bottle to the 8-liter bottle
    if z > 0 and x < 8:
        pour_amount = min(z, 8 - x)
        new_state = (x + pour_amount, y, z - pour_amount)
        actions.append((new_state, pour_amount))   
    
    return actions