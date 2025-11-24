# Pieces (ID, Value)
EMPTY_SQUARE = [0, 0]
WHITE_PAWN = [1, 1]
BLACK_PAWN = [-1,1]
WHITE_ROOK = [2,5]
BLACK_ROOK = [-2,5]
WHITE_KNIGHT = [3,3]
BLACK_KNIGHT = [-3,3]
WHITE_BISHOP = [4,3]
BLACK_BISHOP = [-4,3]
WHITE_QUEEN = [5,9]
BLACK_QUEEN = [-5,9]
WHITE_KING = [6,103]  # 103 is the maximum total value of every piece except the King on one side of the board :)
BLACK_KING = [-6,103]


# Position limits
MIN_ROW_POS = 1
MAX_ROW_POS = 8
MIN_COL_POS = 1
MAX_COL_POS = 8


class Piece:
    def __init__(self, id, value, pos):
        self.__id = id
        self.__value = value
        self.__current_pos = pos
        
    def set_pos(self, new_pos):
        if(new_pos[0] >= MIN_ROW_POS and new_pos[0] <= MAX_ROW_POS):
            self.__current_pos[0] = new_pos[0]
        if(new_pos[1] >= MIN_COL_POS and new_pos[1] <= MAX_COL_POS):
            self.__current_pos[1] = new_pos[1]
        
    def get_pos(self):
        return self.__current_pos

    def set_id(self, id):
        for i in range(0,7):
            if(i == id or -i == id):
                self.__id = id
                return
        self.__id = 0
    
    def get_id(self):
        return self.__id

    def set_value(self, new_value):
        if(new_value == 1 or new_value == 5 or new_value == 3 or new_value == 9 or new_value == 103):
            self.__value = new_value
            return
        self.__value = 0

    def get_value(self):
        return self.__value

    def clear_info(self):
        self.__current_pos = [-1,-1]
        self.__id = 0
        self.__value = 0


class Board:
    def __init__(self):
        self.__current_pcs_pos = []
    
    def __init_pawns(self):
        for i in range(MIN_COL_POS, MAX_COL_POS + 1):
            white_pawn = Piece(WHITE_PAWN[0], WHITE_PAWN[1], [2,i])
            black_pawn = Piece(BLACK_PAWN[0], BLACK_PAWN[1], [7,i])
            self.__current_pcs_pos.append(white_pawn)
            self.__current_pcs_pos.append(black_pawn)  
    
    def __init_rooks(self):
        white_rook_1 = Piece(WHITE_ROOK[0], WHITE_ROOK[1], [1,1])
        white_rook_2 = Piece(WHITE_ROOK[0], WHITE_ROOK[1], [1,8])
        black_rook_1 = Piece(BLACK_ROOK[0], BLACK_ROOK[1], [8,1])
        black_rook_2 = Piece(BLACK_ROOK[0], BLACK_ROOK[1], [8,8])
        self.__current_pcs_pos.append(white_rook_1)
        self.__current_pcs_pos.append(white_rook_2)
        self.__current_pcs_pos.append(black_rook_1)
        self.__current_pcs_pos.append(black_rook_2)
    
    def __init_knights(self):
        white_knight_1 = Piece(WHITE_KNIGHT[0], WHITE_KNIGHT[1], [1,2])
        white_knight_2 = Piece(WHITE_KNIGHT[0], WHITE_KNIGHT[1], [1,7])
        black_knight_1 = Piece(BLACK_KNIGHT[0], BLACK_KNIGHT[1], [8,2])
        black_knight_2 = Piece(BLACK_KNIGHT[0], BLACK_KNIGHT[1], [8,7])
        self.__current_pcs_pos.append(white_knight_1)
        self.__current_pcs_pos.append(white_knight_2)
        self.__current_pcs_pos.append(black_knight_1)
        self.__current_pcs_pos.append(black_knight_2)
    
    def __init_bishops(self):
        white_bishop_1 = Piece(WHITE_BISHOP[0], WHITE_BISHOP[1], [1,3])
        white_bishop_2 = Piece(WHITE_BISHOP[0], WHITE_BISHOP[1], [1,6])
        black_bishop_1 = Piece(BLACK_BISHOP[0], BLACK_BISHOP[1], [8,3])
        black_bishop_2 = Piece(BLACK_BISHOP[0], BLACK_BISHOP[1], [8,6])
        self.__current_pcs_pos.append(white_bishop_1)
        self.__current_pcs_pos.append(white_bishop_2)
        self.__current_pcs_pos.append(black_bishop_1)
        self.__current_pcs_pos.append(black_bishop_2)
    
    def __init_queens(self):
        white_queen = Piece(WHITE_QUEEN[0], WHITE_QUEEN[1], [1,4])
        black_queen = Piece(BLACK_QUEEN[0], BLACK_QUEEN[1], [8,4])
        self.__current_pcs_pos.append(white_queen)
        self.__current_pcs_pos.append(black_queen)
    
    def __init_kings(self):
        white_king = Piece(WHITE_KING[0], WHITE_KING[1], [1,5])
        black_king = Piece(BLACK_KING[0], BLACK_KING[1], [8,5])
        self.__current_pcs_pos.append(white_king)
        self.__current_pcs_pos.append(black_king)
    
    def init_board(self):
        # Init pawns position
        self.__init_pawns()
        
        # Init rooks position
        self.__init_rooks()
        
        # Init knights position
        self.__init_knights()
        
        # Init bishops position
        self.__init_bishops()
        
        # Init queens position
        self.__init_queens()
        
        #Init kings position
        self.__init_kings()

    def update_piece_pos(self, old_pos, new_pos):
        for p in self.__current_pcs_pos:
            if(p.get_pos() == old_pos):
                p.set_pos(new_pos)

    def get_current_pcs_pos(self):
        return self.__current_pcs_pos
    
    def remove_piece_from_board(self, pos):
        for p in self.__current_pcs_pos:
            if(p.get_pos() == pos):
                p.clear_info()
                break
    

class Ruleset:
    def __init__(self):
        self.__piece_state = []
    
    def __get_pcs_index_on_pos(self, piece_pos):
        for index in range (0, len(self.__piece_state)):
            if(self.__piece_state[index].get_pos() == piece_pos):
                return index
        return -1
    
    def __get_valid_pawn_moves(self, index, is_white):
        valid_moves = []
        if (is_white):
            # TODO
            return valid_moves
        # else (black pawns)
        
        return valid_moves
    
    def __get_valid_rook_moves(self, index):
        # --- is_valid_direction note ---
        # 1 -> MSB (Check left moves validity)
        # 1        (Check right moves validity)
        # 1        (Check up moves validity)
        # 1 -> LSB (Check down moves validity)
        is_valid_direction = 0xF
        valid_moves = []
        rook_pos = self.__piece_state[index].get_pos()
        rook_id = self.__piece_state[index].get_id()
        increment_move = 1
        
        while(is_valid_direction & 0x0F):
            if(is_valid_direction & 0x8): # Check if left moves is valid
                if(rook_pos[1]-increment_move >= MIN_COL_POS):
                    index_on_next_square = self.__get_pcs_index_on_pos([rook_pos[0], rook_pos[1]-increment_move])
                    if(index_on_next_square == -1):
                        valid_moves.append([rook_pos[0], rook_pos[1]-increment_move])
                    else:
                        is_valid_direction = is_valid_direction & 0x7
                        if(self.__piece_state[index_on_next_square].get_id() ^ rook_id < 0):
                            valid_moves.append([rook_pos[0], rook_pos[1]-increment_move])
                else:
                    is_valid_direction = is_valid_direction & 0x7
            
            if(is_valid_direction & 0x4): # Check if right moves is valid
                if(rook_pos[1]+increment_move <= MAX_COL_POS):
                    index_on_next_square = self.__get_pcs_index_on_pos([rook_pos[0], rook_pos[1]+increment_move])
                    if(index_on_next_square == -1):
                        valid_moves.append([rook_pos[0], rook_pos[1]+increment_move])
                    else:
                        is_valid_direction = is_valid_direction & 0xB
                        if(self.__piece_state[index_on_next_square].get_id() ^ rook_id < 0):
                            valid_moves.append([rook_pos[0], rook_pos[1]+increment_move])
                else:
                    is_valid_direction = is_valid_direction & 0xB
                    
            if(is_valid_direction & 0x2): # Check if up moves is valid
                if(rook_pos[0]+increment_move <= MAX_ROW_POS):
                    index_on_next_square = self.__get_pcs_index_on_pos([rook_pos[0]+increment_move, rook_pos[1]])
                    if(index_on_next_square == -1):
                        valid_moves.append([rook_pos[0]+increment_move, rook_pos[1]])
                    else:
                        is_valid_direction = is_valid_direction & 0xD
                        if(self.__piece_state[index_on_next_square].get_id() ^ rook_id < 0):
                            valid_moves.append([rook_pos[0]+increment_move, rook_pos[1]])
                else:
                    is_valid_direction = is_valid_direction & 0xD
                    
            if(is_valid_direction & 0x1): # Check if down moves is valid
                if(rook_pos[0]-increment_move >= MIN_ROW_POS):
                    index_on_next_square = self.__get_pcs_index_on_pos([rook_pos[0]-increment_move, rook_pos[1]])
                    if(index_on_next_square == -1):
                        valid_moves.append([rook_pos[0]-increment_move, rook_pos[1]])
                    else:
                        is_valid_direction = is_valid_direction & 0xE
                        if(self.__piece_state[index_on_next_square].get_id() ^ rook_id < 0):
                            valid_moves.append([rook_pos[0]-increment_move, rook_pos[1]])
                else:
                    is_valid_direction = is_valid_direction & 0xE
                
            increment_move = increment_move + 1
        
        return valid_moves
    
    def __get_valid_knight_moves(self, index):
        pass
    
    def __get_valid_bishop_moves(self, index):
        pass
    
    def __get_valid_queen_moves(self, index):
        pass
    
    def __get_valid_king_moves(self, index):
        pass
    
    def get_valid_moves(self, piece_pos, current_board_state):
        self.__piece_state = current_board_state          
        index = self.__get_pcs_index_on_pos(piece_pos)
        id = self.__piece_state[index].get_id()
        next_moves = []
        
        if(id == WHITE_PAWN[0]):
            next_moves = self.__get_valid_pawn_moves(index, 1)
            
        elif(id == BLACK_PAWN[0]):
            next_moves = self.__get_valid_pawn_moves(index, 0)
        
        elif(id == WHITE_ROOK[0] or id == BLACK_ROOK[0]):
            next_moves = self.__get_valid_rook_moves(index)
        
        elif(id == WHITE_KNIGHT[0] or id == BLACK_KNIGHT[0]):
            next_moves = self.__get_valid_knight_moves(index)
        
        elif(id == WHITE_BISHOP[0] or id == BLACK_BISHOP[0]):
            next_moves = self.__get_valid_bishop_moves(index)
        
        elif(id == WHITE_QUEEN[0] or id == BLACK_QUEEN[0]):
            next_moves = self.__get_valid_queen_moves(index)
        
        elif(id == WHITE_KING[0] or id == BLACK_KING[0]):
            next_moves = self.__get_valid_king_moves(index)
        
        return next_moves


class Chess:
    def __init__(self):
        self.__board = Board()
        self.__board.init_board()
        self.__rules = Ruleset()
    
    def test(self):
        self.__board.remove_piece_from_board([2,1])
        pieces_pos = self.__board.get_current_pcs_pos()
        for p in pieces_pos:
            print(p.get_pos())
        print("Valid rook moves")
        moves = self.__rules.get_valid_moves([1,1], self.__board.get_current_pcs_pos())
        print(moves)
    
    def run_chess(self):
        pass