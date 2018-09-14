class Board:
    no_of_queens = 0
    def __init__(self):
        self.no_of_queens = 0
        self.all_positions = {}
        self.all_positions = self.generate_all_positions()
        self.unattacked_positions = self.generate_all_positions()
        self.legal_moves = self.generate_all_positions()
    
    def place_queen(self, position):
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] == "Queen" :
            print(f'cant place queen on {self.all_positions.get(position)}')
            return
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] != "Attacked":
            self.all_positions.get(position)['Status'] = "Queen"
            self.no_of_queens = self.no_of_queens + 1
            self.generate_attack_moves(position)
        else:
            print(f'cant place queen on {self.all_positions.get(position)}')
            return

    
    def remove_queen(self, position):
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] == "Not_Attacked" :
            print(f'cant remove queen from {self.all_positions.get(position)}')
            return
        if self.all_positions.get(position) and self.all_positions.get(position)['Status'] == "Queen":
            self.all_positions.get(position)['Status'] = "Not_Attacked"
            self.no_of_queens = self.no_of_queens - 1
            print(f'removed queen from {self.all_positions.get(position)}')

    def number_of_queens(self):
        return self.no_of_queens
    
    def has_8_queens(self):
        return True if self.number_of_queens() > 8 else False 


    
    def generate_all_positions(self):
        for i in range(0,8):
            for j in range(0,8):
                key = 'P' + str(i)+str(j)
                self.all_positions[key] = { 'x':i, 'y':j, 'Status':'Not_Attacked' }
        return self.all_positions

    def attack(self, px, py):
        point = 'P' + str(px) + str(py)
        if self.legal_moves.get(point) and self.legal_moves.get(point)['Status'] != "Queen":
            self.unattacked_positions[point]['Status'] = "Attacked"
        return

    def generate_attack_moves(self, pos):
        for i in range(7):
            x = int(pos[1])
            y = int(pos[-1])
            #generate attacking moves for North, south, East, West directions
    
            px = x + i
            py = y
            
            self.attack(px,py)

            px = x
            py = y + i
            
            self.attack(px,py)


            px = x - i
            py = y
            
            self.attack(px,py)

            px = x
            py = y - i
            
            self.attack(px,py)

            #generate attacking moves for Diagonals Directions, (North East, North West, South East, South West)

            px = x + i
            py = y + i
            
            self.attack(px,py)

            px = x - i
            py = y - i
            
            self.attack(px,py)

            px = x  - i
            py = y  + i
            
            self.attack(px,py)

            px = x  + i
            py = y  - i
            
            self.attack(px,py)

            
        return self.unattacked_positions
    


board = Board()
board.place_queen("P22");
board.place_queen("P44");
board.remove_queen("P22");
board.place_queen("P44");
board.remove_queen("P43");
board.remove_queen("P43");
board.place_queen("P77");
