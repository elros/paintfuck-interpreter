def cycle_capped(value, low, top):
    if value < low:
        return top - 1
    if value >= top:
        return low
    return value


def bitfield_to_str(field):
    return '\r\n'.join(
        ''.join(str(int(bit)) for bit in row)
        for row in field
    )
