from SudokuGame import SudokuGame

# region Menu functions
def Menu():
    print('''
    -----------  MENU  --------------
    [0] Exit
    [1] Option 1:\tStart a new game [genarate]
    [2] Option 2:\tShow datas about table
    [3] Option 3:\tPrint table
    [4] Option 4:\tPrint table just nums [Every size]
    [5] Option 5:\tPrint the original table (just with nums) [Every size]
    [6] Option 6:\tSolve sudoku with powershell subprocess
    ----------------------------------''')
    MenuRun()


def MenuRun():
    try:
        option = int(input("Enter your option: "))
    except ValueError as err:
        print(err)
        MenuRun()

    if option == 0:
        exit()

    while option != 0:
        if option == 1:
            print("-- option 1 --")
            NewGame()
            PrintTable()
            Menu()

        elif option == 2:
            print("-- option 2 --")
            ShowDatasAboutATable(game1)
            Menu()

        elif option == 3:
            print("-- option 3 --")
            PrintTable()
            Menu()

        elif option == 4:
            print("-- option 4 --")
            PrintTableJNums()
            Menu()

        elif option == 5:
            print("-- option 5 --")
            PrintOrigin()
            Menu()

        elif option == 6:
            print("-- option 6 --")
            CallSolverFromPS()
            Menu()

        else:
            print("Invalid option!")
            Menu()
    print()


def NewGame():
    tableS = 4
    regionS = 2
    diff = 1

    try:
        diff = int(input('''
        Type in difficulty level!
        Easy = 1 [default], Medium = 2, Hard = 3 \n'''))
    except ValueError or UnboundLocalError as err:
        print(err)

    if diff not in [1, 2, 3]:
        diff = 1

    try:
        tableS = int(input("Enter TableSize! (4 [default]/9/16/25): \n"))
    except ValueError or UnboundLocalError as err:
        print(err)

    if tableS not in [4, 9, 16, 25]:
        tableS = 4

    if tableS == 4:
        regionS = 2
        print("Your regionSize is 2")
    elif tableS == 9:
        regionS = 3
        print("Your regionSize is 3")
    elif tableS == 16:
        regionS = 4
        print("Your regionSize is 4")
    elif tableS == 25:
        regionS = 5
        print("Your regionSize is 5")
    else:
        print("Bad size")

    try:
        game1.NewGame(tableS, regionS, diff)
    except ValueError or UnboundLocalError as err:
        print(err)


def ShowDatasAboutATable(game):
    print("--show_datas_about_a_table--")
    print("TableSize: " + str(game._table.Size()))
    print("RegionsSize: " + str(game._table.RegionSize()))
    print("isFilled: " + str(game._table.IsFilled()))
    print("Difficulty: " + str(game1._gameDifficulty))
    print("-__-")


def PrintTable():
    if game1._table.Size() == 4 or game1._table.Size() == 9:
        PrintTableJNums()
    elif game1._table.Size() == 16:
        PrintTableWLetters()
    elif game1._table.Size() == 25:
        PrintTableJLetters()
    else:
        print("Error")


def PrintTableWLetters():
    game1.PrintTableWithLetters()


def PrintTableJLetters():
    game1.PrintTableJustLetters()


def PrintTableJNums():
    game1.PrintTableJustNums()


def PrintOrigin():
    game1.PrintOriginTable()


def CallSolverFromPS():
    game1.CallSolverFromPS()
# endregion


# region Main
print("\t---- Game started ----")
diff = 1  # Easy
try:
    game1 = SudokuGame(4, 2, diff)
    game1.NewGame(4, 2, diff)
except ValueError as err:
    print(err)
    exit()
# menu
Menu()
# endregion
