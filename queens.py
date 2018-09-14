all_positions = {}
def generate_all_positions():
    for i in range(0,8):
        for j in range(0,8):
            key = 'P' + str(i)+str(j)
            all_positions[key] = { 'x':i, 'y':j, 'Status':'Not_Attacked' }
    return all_positions
unattacked_positions = generate_all_positions()
legal_moves = generate_all_positions()

def generate_attack_moves(pos):
    seen = {}
    for i in range(7):
        x = int(pos[1])
        y = int(pos[-1])
        #generate attacking moves for North, south, East, West directions
        point = ""
        px = x + i
        py = y
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} + {i}, y: {y} + {0} => px: {px}, py: {py}'
        # if  not seen.get(point):
        #     seen[point] = 1
        #     print(point)
        point = ""
        px = x
        py = y + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
        #     # del(unattacked_positions[point])
        # point = point + f' x: {x} + {0}, y: {y} + {i} => px: {px}, py: {py}'
        # if  not seen.get(point):
        #     seen[point] = 1
        #     print(point)
        point = ""
        px = x - i
        py = y
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} - {i}, y: {y} + {0} => px: {px}, py: {py}'
        # if not seen.get(point):
        #     seen[point] = 1
        #     print(point)
        point = ""
        px = x
        py = y - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # if not seen.get(point):
        #     seen[point] =  1
        #     point = point + f' x: {x} + {0}, y: {y} - {i} => px: {px}, py: {py}'
        #     print(point)
        #generate diagonal directional moves for Queen.
        point = ""
        px = x + i
        py = y + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} + {i}, y: {y} + {i} => px: {px}, py: {py}'
        # if not seen.get(point):
        #     seen[point] =  1
        #     print(point)
        point = ""
        px = x - i
        py = y - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} - {i}, y: {y} - {i} => px: {px}, py: {py}'
        # if seen.get(point) == 0:
        #     seen[point] = 1
        #     print(point)
        point = ""
        px = x  - i
        py = y  + i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} - {i}, y: {y} + {i}  => px: {px}, py: {py}'
        # if not seen.get(point):
        #     seen[point] =  1
        #     print(point)
        point = ""
        px = x  + i
        py = y  - i
        point = pos[0] + str(px) + str(py)
        if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
            unattacked_positions[point]['Status'] = "Attacked"
            # del(unattacked_positions[point])
        # point = point + f' x: {x} + {i}, y: {y} - {i}  => px: {px}, py: {py}'
        # if not seen.get(point):
        #     seen[point] =  1
        #     print(point)
        point = ""
        
    return unattacked_positions

def attack(px, py):
    point = 'P' + str(px) + str(py)
    if legal_moves.get(point) and legal_moves.get(point)['Status'] != "Queen":
        unattacked_positions[point]['Status'] = "Attacked"
    return



class Board:
    no_of_queens = 0
    def __init__(self, all_positions):
        self.all_positions = all_positions
        self.no_of_queens = 0
    
    def place_queen(self, position):
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] != "Attacked":
            self.all_positions.get(position)['Status'] = "Queen"
            self.no_of_queens = self.no_of_queens + 1
            generate_attack_moves(position)
        else:
            print(f'cant place queen on {self.all_positions.get(position)}')

    
    def remove_queen(self, position):
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] == "Queen":
            self.all_positions.get(position)['Status'] = "Not_Attacked"
            self.no_of_queens = self.no_of_queens - 1
            print(f'removed queen from {self.all_positions.get(position)}')

    
    def has_8_queens(self):
        return True if no_of_queens > 8 else False 

board = Board(unattacked_positions)

board.place_queen("P33")
board.place_queen("P22")
board.remove_queen("P33")