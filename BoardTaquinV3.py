"""
NOTE : CHATGPT WAS NOT USED IN THE PROCESS OF CREATION OF THESE FILE AND THE ASSOCIATED FILES ,
                 IN THE CONTAINING MODULE NOR ANY OTHER REFERENCES FROM INTERNET NOR BEEN TAKEN FROM ANY OTHER PERSON
                 WORK , ONLY THE OFFICIAL PYTHON DOCUMENTATION BEEN USED AS A REFERENCE .
                 PLEASE DON'T DISTRIBUTE THE CODE FOR THIS TERMINAL MINI-SOFTWARE ON THE INTERNET NOR TO ANYONE
                 WITHOUT PERMISSION .
                 MY REGARDS .
                 AUTHOR : "HASSEN HAMDI" .
"""

from random import shuffle


class Taquin:
    def __init__(self, board: list = None, node=None, saisi: bool = None):
        """
        Constructor method that allow instantiation of new 'Taquin' Object to link the existing current
        node with its neighbor in correspondence to the next possible move direction .
        """
        self.generated_nodes_number = None
        self.posCase0: int = None  # variable holding the position of the empty case declared as 'None' to be used further .
        self.current: list = None  # matrix holding the current value of the puzzle .
        self.previous_move: str = None  # a variable that note the move from the previous state to the current one.
        self.previous_node = None
        #  These attributes (links as 'pointers') define the successors of the current state depending on the list of all
        #  the  possible moves that can be applied from the current state ( Node ) .
        self.right = None
        self.down = None
        self.left = None
        self.up = None

        if board and not saisi:
            self.current = board
            self.positioncasevide()
            self.previous_node = node

        elif saisi:
            print("debug")
            self.saisie_noeud_initial()
            self.positioncasevide()
        else:
            # a list created with list comprehension that contain int from 0 to 8 , 9 element in total .
            number = [x for x in range(9)]
            # the shuffle function from random module were used to be change the order of the number in the list .
            shuffle(number)
            self.current = number.copy()
            self.positioncasevide()

    def afficher_taquin(self):
        if self.current is None:
            return
        ec = self.posCase0
        self.current[ec] = " "
        print(f"+---+---+---+",
              f"| {self.current[0]} | {self.current[1]} | {self.current[2]} |",
              f"+---+---+---+",
              f"| {self.current[3]} | {self.current[4]} | {self.current[5]} |",
              f"+---+---+---+",
              f"| {self.current[6]} | {self.current[7]} | {self.current[8]} |",
              f"+---+---+---+", "", sep="\n")

        self.current[ec] = 0
        del ec

    def positioncasevide(self):
        self.posCase0 = self.current.index(0)
        # using formulas to transform the list indices to matrix coord row=p//3,col=p%3

    def numero(self, r, c):
        return self.current[3 * r + c]

    def saisie_noeud_initial(self):
        self.current = list()
        for i in range(3):
            for j in range(3):
                val = input(f"Please type the value of matrix case (row = {i} , col = {j}) :  ")
                self.current.append(int(val))
