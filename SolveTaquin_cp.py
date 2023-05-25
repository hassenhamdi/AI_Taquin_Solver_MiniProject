"""
NOTE : CHATGPT WAS NOT USED IN THE PROCESS OF CREATION OF THESE FILE AND THE ASSOCIATED FILES ,
                 IN THE CONTAINING MODULE NOR ANY OTHER REFERENCES FROM INTERNET NOR BEEN TAKEN FROM ANY OTHER PERSON
                 WORK , ONLY THE OFFICIAL PYTHON DOCUMENTATION BEEN USED AS A REFERENCE .
                 PLEASE DON'T DISTRIBUTE THE CODE FOR THIS TERMINAL MINI-SOFTWARE ON THE INTERNET NOR TO ANYONE
                 WITHOUT PERMISSION .
                 THE CODE IS COMMENTED IN ENGLISH .
                 MY REGARDS .
                 AUTHOR : "HASSEN HAMDI" .
                 .
"""
import itertools
import os
import pickle
from math import inf
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from pickle import load, dump
from time import sleep, strftime
from pip._internal.cli import spinners
from BoardTaquinV3 import *


class SolveTaquin:
    #  Class attribute
    finalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    def __init__(self, node, arg: bool = False):
        #  Instance(object) specific attributes
        self.explored_nodes_list = list()
        self.limit = inf
        self.generatedNodeNumber = 0
        self.searchTreeDepth = 0
        self.step_to_solution_counter: int = 0
        self.path = None
        self.solution_node_depth = 0
        self.root_dumpfile = None
        self.count = 0
        self.step_to_solution_counter = 0
        self.root: Taquin = node
        self.node: Taquin = node
        self.neighbor = None
        self.solved = None
        self.solution_node: Taquin = None
        self.exploring_space = []
        self.dump_or_load(arg)
        self.solution_path_saver()

    def load(self, root_dmp=Path("dmp/default.dmp")):
        try:
            print("Please pick the file you want to load from the list below :")
            os.chdir("dmp")
            for file in os.listdir():
                file = file.removesuffix(".dmp")
                print("\t"+file)
            os.chdir("..")
            filename = input("file name :   ")

            if len(filename) == 27:
                path = "dmp/" + filename + ".dmp"
                root_dmp = Path(path)
            if root_dmp.exists():
                self.root_dumpfile = root_dmp.open("r+b")
                self.root = load(self.root_dumpfile)
                self.root_dumpfile.close()
                self.neighbor_list_update(self.root)
                print(f"dump file '{filename}' loaded successfully !\n")
                os.system("pause")
            else:
                inp = input("File not found !\nPlease try to type correctly an existing file name\nContinue ? (y/n) : ")
                if inp[0] == "y":
                    self.load()
                else:
                    print("The loading operation was aborted ")
                    print("The program will exist .")
                    exit()

        except pickle.PickleError or EOFError:
            print("loading error ")
            os.system("pause")
            exit()

    def dump(self, root_dmp_path="dmp/default.dmp"):
        try:
            path = Path(root_dmp_path)
            if path.exists():
                return
            self.root_dumpfile = path.open("w+b")
            dump(self.root, self.root_dumpfile)

            print(f"Result was saved successfully to \"{root_dmp_path}\"")
        except pickle.PickleError:
            print(Exception)
            os.system("pause")
            exit()

    def dump_or_load(self, arg):

        p = Path("dmp/default.dmp")
        if arg:
            if p.exists():
                print("Default dump file found .")
                self.load()
            else:
                print(f"Missing 'dmp/default.dmp' file .")
                print("Creating new file.")
                sleep(1)
                self.root_dumpfile = p.open("w+b")
                print("Generating the exploring-space in 3 secs press Ctrl+C to exit.")
                sleep(3)
                self.generating_in_progress()

            return

        # storing the result in binary file
        self.generating_in_progress()  # contain the dump method for autosave .

    def neighbor_list_update(self, node):
        self.neighbor = [node.right, node.down, node.left, node.up]

    def isvalid(self, node):
        if node.current == self.finalState:
            return True
        return False

    def transitions(self):
        #  Local Variables declaration
        nbmvt = 0  # variable that store the number of the possible move from the current state .
        possible_move = []  # will store the coords of the adjacent cell of board .
        r = self.node.posCase0 // 3  # r is the row number of the empty case .
        c = self.node.posCase0 % 3  # c is the column number of the empty case .

        match r:
            # match is keyword similar to switch in java , c and c++ but is used to be compared to the pattern
            # (as in regular expression ER TLA ) present in the case statement .
            case 0:  # At the top row the empty cell can move only "down" which mean current row + 1
                r1 = r + 1
                c1 = c  # the column number remain the same
                mvt = 3 * r1 + c1  # the tuple mvt contain the coord that the empty cell can move to .
                possible_move.append((mvt, "down"))  # appending the coord to the list of possible movements
                # from the current position of empty cell in the current state .
                nbmvt += 1
            case 2:  # At the bottom the empty cell can move "up" , which mean row-1 .
                r1 = r - 1
                c1 = c
                mvt = 3 * r1 + c1
                possible_move.append((mvt, 'up'))
                nbmvt += 1
            case 1:  # In the middle the empty cell can move in both directions .
                r1 = r + 1
                r2 = r - 1
                c1 = c
                mvt1 = 3 * r1 + c1  # down
                mvt2 = 3 * r2 + c1  # up
                possible_move.append((mvt1, 'down'))
                possible_move.append((mvt2, 'up'))
                nbmvt += 2

        match c:  # the same logic used in the previous match expression above with the row number ,
            # here [('top' and 'up') are 'left'] and [('bottom' and 'down') are 'right']
            case 0:
                c1 = c + 1
                r1 = r
                mvt = 3 * r1 + c1
                possible_move.append((mvt, 'right'))
                nbmvt += 1
            case 2:
                c1 = c - 1
                r1 = r
                mvt = 3 * r1 + c1
                possible_move.append((mvt, 'left'))
                nbmvt += 1
            case 1:
                c1 = c + 1
                c2 = c - 1
                r1 = r
                mvt1 = 3 * r1 + c1
                mvt2 = 3 * r1 + c2
                nbmvt += 2
                possible_move.append((mvt1, 'right'))
                possible_move.append((mvt2, 'left'))

        # print("start")
        for i in range(nbmvt):
            pmd = possible_move[i][1]
            neighbor = self.permuter(possible_move[i][0])
            if neighbor in self.exploring_space:  # this what solved the cycling
                continue
            self.next_state(pmd, neighbor)

    def next_state(self, next_state, neighbor):
        match next_state:
            case 'right':
                self.node.right = Taquin(neighbor, self.node)
                self.neighbor[0] = self.node.right
            case 'down':
                self.node.down = Taquin(neighbor, self.node)
                self.neighbor[1] = self.node.down

            case 'left':
                self.node.left = Taquin(neighbor, self.node)
                self.neighbor[2] = self.node.left

            case 'up':
                self.node.up = Taquin(neighbor, self.node)
                self.neighbor[3] = self.node.up

    def permuter(self, case2: int) -> list:
        # to be use in the above method to generate the neighbor state :
        # case1 contain the coordination of '0'
        """
                :rtype:list
                a function that take the indices of case1==the empty case and case2 coord of the adjacent case
                and switch the content of each cell
        """

        t_copy = self.node.current.copy()  # make copy of the current state.
        t_copy[self.node.posCase0] = self.node.current[case2]  # overwrite the value of case1 with the value of case2.
        t_copy[case2] = 0  # affecting the value of case1 to case2 --> '0' .
        return t_copy

    def terminal_text(self, g=None, output_text=None, style="material"):
        if output_text is None:
            output_text = f"Generating the exploring-space is in progress"
        count = spinners.InteractiveSpinner(output_text, min_update_interval_seconds=0.15)
        count._spin_cycle = itertools.cycle([f"\n{self.count} Node was Generated"])

        while g.running():
            count.spin()
            count._spin_cycle = itertools.cycle([f"{self.count} Node was Generated"])

    def generating_in_progress(self):
        with ThreadPoolExecutor(max_workers=2) as p:
            g = p.submit(self.generate_neighbor)
            t = p.submit(self.terminal_text, g)

    def generate_neighbor(self):
        q = [self.root]  # queue
        while q:
            self.node = q.pop(0)
            self.exploring_space.append(self.node.current)
            self.neighbor_list_update(self.node)

            if self.isvalid(self.node):
                self.root.generated_nodes_number = self.count
                self.dump(root_dmp_path="dmp/"+str(self.root.current)+".dmp")
                self.solution_node = self.node
                self.solution_path_saver()
                break

            self.transitions()

            for n in self.neighbor:
                if n is not None:
                    if n.current in self.exploring_space:
                        continue
                    q.append(n)
                    self.count += 1

        print(f"Neighbor Tree Generated ! count : {self.count}\n")

    def solve(self):
        self.step_to_solution_counter = 0
        search_type = input("Search method : DFS(1) , Limited DFS (2), BFS(3) , Heuristic Search A*(4) : ")
        match search_type:
            case "1":
                print("\nSolving with DFS")
                self.recursive_dfs(self.root)
            case "2":
                while not self.solved:
                    print("Solving with limited DFS")
                    self.limit = int(input("Please type the depth search :\t"))
                    print()
                    self.recursive_dfs(self.root, 0)
                    if self.solved:
                        break

                    _continue = input("Type 'q' and ENTER to exit ,'s' to change search method  or any to continue :")
                    if _continue == "q":
                        break
                    if _continue == "s":
                        self.solve()
            case "3":
                print("\nSolving with BFS :")
                self.bfs()
            case "4":
                print("\nSolving with A* : ")
                self.heuristic_search(self.root)
            case _:
                self.solve()  # default option in case the user type a value different from the case above .
                return

        if self.solved:
            # todo adding option to use another search algorithm
            self.solution_path_saver()

    def heuristic_search(self, n, depth_level=0):
        self.step_to_solution_counter += 1
        """
        A* search method for optimal time and space complexity .
        with optimized cost calculation formula.
        :return:
        """
        if n is None:
            return None

        self.node = n
        self.node.afficher_taquin()

        if self.isvalid(n):
            print("Solution Found !")
            self.solution_node = n
            self.solved = True
            return True

        min_cost = 10 + depth_level
        next_node = list()
        if not depth_level:
            self.node = self.root

        self.neighbor_list_update(self.node)
        for node in self.neighbor:
            if node:
                cost = self._cost(node, depth_level)
                if cost < min_cost:
                    min_cost = cost
                    next_node = [node]

        for node in self.neighbor:
            if node:
                cost = self._cost(node, depth_level)
                if cost <= min_cost and not (node in next_node):
                    next_node.append(node)
        for node in next_node:
            if not self.solved:
                self.heuristic_search(node, depth_level + 1)

    def recursive_dfs(self, node, depth_level=0):

        self.node = node

        if node is None:
            return False
        else:
            self.explored_nodes_list.append(node)
            print(f"Node at depth level : {depth_level}")
            self.node.afficher_taquin()

        if depth_level == self.limit:
            return

        if self.isvalid(self.node):
            self.solution_node = self.node
            self.solution_node_depth = depth_level
            self.node.afficher_taquin()
            print("Solution found !")
            self.solved = True
            print(f"step count = {self.step_to_solution_counter}")
            return True

        self.neighbor_list_update(self.node)

        for n in self.neighbor:
            if n is not None:
                self.step_to_solution_counter += 1
                r = self.recursive_dfs(n, depth_level+1)
                if r:
                    return True

                if depth_level < self.limit:
                    self.explored_nodes_list.append(node)
                    print(f"Backstep : Depth level ({depth_level}) \n")

        if not self.solved and depth_level == 0:
            print(f"Solution not found with {self.limit} as depth limit . ")

    def iterative_dfs(self, limit=inf) -> None:
        counter = 0
        stack = list()
        stack.append(self.root)
        self.explored_nodes_list = [self.root]

        while stack and counter <= limit:
            self.step_to_solution_counter += 1
            self.node = stack.pop()
            self.neighbor_list_update(self.node)
            self.node.afficher_taquin()
            if self.isvalid(self.node):
                self.solved = True
                self.solution_node = self.node
                print(f"Solution Found! in {self.step_to_solution_counter} step ")
                break
            for n in self.neighbor:
                if n:
                    self.explored_nodes_list.append(n)
                    stack.append(n)

            counter += 1

        if not self.solved:
            print("Solution not found .")

    def path_printer(self, secs=0):  # the default option is 0 secs for consecutive printing without waiting but
        #  I did give 1 as value in the call at the main thread main.py
        print("Path to the Solution :")
        sleep(3)
        for node in self.path:
            sleep(secs)
            node.afficher_taquin()

    def solution_path_saver(self):
        if self.solution_node is None:
            return

        print("\nSaving the path to the Solution .")
        self.path = []
        bottom_top = self.solution_node
        while bottom_top:
            self.path.insert(0, bottom_top)
            bottom_top = bottom_top.previous_node
        self.root = self.path[0]
        self.searchTreeDepth = len(self.path) - 1

    def iterative_dfs_depth_limited(self, limit: int) -> None:
        self.iterative_dfs(limit)

    def _cost(self, node, depth_level):
        return depth_level + self._h(node.current)

    def _h(self, current):
        heuristic_sum: int = 0

        for ele in current:
            #  first calculation of the abs value of difference between the current and the final state elements
            #  which range from 0 to 8
            tmp = abs(current.index(ele) - self.finalState.index(ele))
            #  second adding 'the quotient' --> (row number), and the rest --> (column number)  of  the value stored
            #  in 'tmp' for each element to heuristic_sum which represent the amount/level of the disorder of the
            #  current state
            heuristic_sum += tmp // 3 + tmp % 3
        return heuristic_sum

    def bfs(self):
        queue_ = list()
        queue_.append(self.root)
        while queue_:
            self.step_to_solution_counter += 1
            self.node = queue_.pop(0)
            self.neighbor_list_update(self.node)
            self.node.afficher_taquin()
            if self.isvalid(self.node):
                self.solved = True
                self.solution_node = self.node
                print("valid")
                print(f"Solution Found! in {self.step_to_solution_counter} step ")
                break
            for n in self.neighbor:
                if n:
                    queue_.append(n)
