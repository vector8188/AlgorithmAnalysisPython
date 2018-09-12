all_positions = {}
def generate_all_positions():
    for i in range(0,9):
        for j in range(0,9):
            key = 'P' + str(i)+str(j)
            all_positions[key] = { 'x':i, 'y':j }
    return all_positions
unattacked_positions = generate_all_positions()
legal_moves = generate_all_positions()

def generate_attack_moves(pos):
    seen = {}
    for i in range(8):
        x = int(pos[1])
        y = int(pos[-1])
        #generate attacking moves for North, South, East, West directions
        point = ""
        px = x + i
        py = y
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} + {i}, y: {y} + {0} => px: {px}, py: {py}'
        if  not seen.get(point):
            seen[point] = 1
            print(point)
        point = ""
        px = x
        py = y + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} + {0}, y: {y} + {i} => px: {px}, py: {py}'
        if  not seen.get(point):
            seen[point] = 1
            print(point)
        point = ""
        px = x - i
        py = y
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} - {i}, y: {y} + {0} => px: {px}, py: {py}'
        if not seen.get(point):
            seen[point] = 1
            print(point)
        point = ""
        px = x
        py = y - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        if not seen.get(point):
            seen[point] =  1
            point = point + f' x: {x} + {0}, y: {y} - {i} => px: {px}, py: {py}'
            print(point)
        #generate diagonal directional moves for Queen.
        point = ""
        px = x + i
        py = y + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} + {i}, y: {y} + {i} => px: {px}, py: {py}'
        if not seen.get(point):
            seen[point] =  1
            print(point)
        point = ""
        px = x - i
        py = y - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} - {i}, y: {y} - {i} => px: {px}, py: {py}'
        if seen.get(point) == 0:
            seen[point] = 1
            print(point)
        point = ""
        px = x  - i
        py = y  + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} - {i}, y: {y} + {i}  => px: {px}, py: {py}'
        if not seen.get(point):
            seen[point] =  1
            print(point)
        point = ""
        px = x  + i
        py = y  - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point):
            del(unattacked_positions[point])
        point = point + f' x: {x} + {i}, y: {y} - {i}  => px: {px}, py: {py}'
        if not seen.get(point):
            seen[point] =  1
            print(point)
        point = ""
        
    return unattacked_positions
print(generate_attack_moves('P45'))



        