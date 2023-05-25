"""
NOTE : CHATGPT WAS NOT USED IN THE PROCESS OF CREATION OF THESE FILE AND THE ASSOCIATED FILES ,
                 IN THE CONTAINING MODULE NOR ANY OTHER REFERENCES FROM INTERNET NOR BEEN TAKEN FROM ANY OTHER PERSON
                 WORK , ONLY THE OFFICIAL PYTHON DOCUMENTATION BEEN USED AS A REFERENCE .
                 PLEASE DON'T DISTRIBUTE THE CODE FOR THIS TERMINAL MINI-SOFTWARE ON THE INTERNET NOR TO ANYONE
                 WITHOUT PERMISSION .
                 MY REGARDS .
                 AUTHOR : "HASSEN HAMDI" .
"""
from SolveTaquin_cp import *

if __name__ == '__main__':
    os.system("cls")
    solve_var = None
    root = None
    generate_or_load = input("Type the matrix values (1) Generate random root node for the puzzle (2) or load " +
                             f"an existing one (3) ? (1/2/3)\n")
    mistype_number = 0
    while generate_or_load not in ('1', '2', '3') and mistype_number < 3:
        generate_or_load = input("Please type (1) for manual input (2) to generate random and (3) for loading " +
                                 "an exiting one .\n")
        mistype_number += 1

    if mistype_number == 3:
        exit("Mistype error number exceeded , the process instance terminated .")

    if generate_or_load in ('1', '2'):
        if generate_or_load == '2':
            root = Taquin()
        else:
            root = Taquin(saisi=True)

        print("Start generating.")
        os.system("pause")
        print("Starting generating exploring-space .")
        start_time = strftime('%X')
        print(f"Start time : {start_time}")
        solve_var = SolveTaquin(root)
        print("\nGenerating ended")
        print(f"end time : {strftime('%X')}")

    elif generate_or_load == '3':
        solve_var = SolveTaquin(None, True)
        root = solve_var.root
        if root:
            print("\n", f"The total number of generated nodes (states) is : {root.generated_nodes_number}")
        else:
            root = Taquin()
    print("\n", "Start solving.")
    os.system('pause')

    print("\nPlease choose a search method from the list below to solve the puzzle : ")
    solve_var.solve()
    print(f"\nTotal number of the explored Node is : {solve_var.step_to_solution_counter}")
    if solve_var.solved:
        print("\nPrint the path to the solution node.")
        os.system("pause")
        solve_var.path_printer(1)
