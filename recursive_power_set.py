def recursive_power_set(items):
    if type(items) == list:
        set_items = set()
        for i in items:
            set_items.add(i)
            ps = set_items
    else:
        ps = items
    for e in set_items:
        ps = set_items.remove(e)
        ps.update(recursive_power_set(ps))
        ps.add(e)
    return ps

print (recursive_power_set([1,2,3]))

