def ScallingDomain(x, old_min, old_max, new_min, new_max):
    A_new = ((x - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
    return A_new


# print(ScallingDomain(0.81,0,1,0,3))