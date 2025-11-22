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
WHITE_KING = [6,103]  # 103 is the total value of every piece except the King on one side of the board :)
BLACK_KING = [-6,103]


# Position limits
MIN_ROW_POS = 1
MAX_ROW_POS = 8
MIN_COL_POS = 1
MAX_COL_POS = 8


class Piece:
    def __init__(self, id, value, pos):
        self.id = id
        self.value = value
        self.current_pos = pos
        
    def set_pos(self, new_pos):
        self.current_pos = new_pos
        
    def get_pos(self):
        return self.current_pos

class Board:
    def __init__(self):
        self.current_pcs_pos = []
    
    def __init_pawns(self):
        for i in range(MIN_COL_POS, MAX_COL_POS + 1):
            white_pawn = Piece(WHITE_PAWN[0], WHITE_PAWN[1], [2,i])
            black_pawn = Piece(BLACK_PAWN[0], BLACK_PAWN[1], [7,i])
            self.current_pcs_pos.append(white_pawn)
            self.current_pcs_pos.append(black_pawn)  
    
    def __init_rooks(self):
        white_rook_1 = Piece(WHITE_ROOK[0], WHITE_ROOK[1], [1,1])
        white_rook_2 = Piece(WHITE_ROOK[0], WHITE_ROOK[1], [1,8])
        black_rook_1 = Piece(BLACK_ROOK[0], BLACK_ROOK[1], [8,1])
        black_rook_2 = Piece(BLACK_ROOK[0], BLACK_ROOK[1], [8,8])
        self.current_pcs_pos.append(white_rook_1)
        self.current_pcs_pos.append(white_rook_2)
        self.current_pcs_pos.append(black_rook_1)
        self.current_pcs_pos.append(black_rook_2)
    
    def __init_knights(self):
        white_knight_1 = Piece(WHITE_KNIGHT[0], WHITE_KNIGHT[1], [1,2])
        white_knight_2 = Piece(WHITE_KNIGHT[0], WHITE_KNIGHT[1], [1,7])
        black_knight_1 = Piece(BLACK_KNIGHT[0], BLACK_KNIGHT[1], [8,2])
        black_knight_2 = Piece(BLACK_KNIGHT[0], BLACK_KNIGHT[1], [8,7])
        self.current_pcs_pos.append(white_knight_1)
        self.current_pcs_pos.append(white_knight_2)
        self.current_pcs_pos.append(black_knight_1)
        self.current_pcs_pos.append(black_knight_2)
    
    def __init_bishops(self):
        white_bishop_1 = Piece(WHITE_BISHOP[0], WHITE_BISHOP[1], [1,3])
        white_bishop_2 = Piece(WHITE_BISHOP[0], WHITE_BISHOP[1], [1,6])
        black_bishop_1 = Piece(BLACK_BISHOP[0], BLACK_BISHOP[1], [8,3])
        black_bishop_2 = Piece(BLACK_BISHOP[0], BLACK_BISHOP[1], [8,6])
        self.current_pcs_pos.append(white_bishop_1)
        self.current_pcs_pos.append(white_bishop_2)
        self.current_pcs_pos.append(black_bishop_1)
        self.current_pcs_pos.append(black_bishop_2)
    
    def __init_queens(self):
        white_queen = Piece(WHITE_QUEEN[0], WHITE_QUEEN[1], [1,4])
        black_queen = Piece(BLACK_QUEEN[0], BLACK_QUEEN[1], [8,4])
        self.current_pcs_pos.append(white_queen)
        self.current_pcs_pos.append(black_queen)
    
    def __init_kings(self):
        white_king = Piece(WHITE_KING[0], WHITE_KING[1], [1,5])
        black_king = Piece(BLACK_KING[0], BLACK_KING[1], [8,5])
        self.current_pcs_pos.append(white_king)
        self.current_pcs_pos.append(black_king)
    
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
        for p in self.current_pcs_pos:
            if(p.get_pos() == old_pos):
                p.set_pos(new_pos)


class Chess:
    def __init__(self):
        self.board = Board()
        self.board.init_board()
    
    def run_chess(self):
        pass