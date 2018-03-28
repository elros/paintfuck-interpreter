def cycle_capped(value, low, top):
    if value < low:
        return top - 1
    if value >= top:
        return low
    return value
