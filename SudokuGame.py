from math import sqrt
import subprocess
import sys
from SudokuTable import SudokuTable
from enum import Enum
import random
import copy


class GameDifficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


class SudokuGame:
    from SudokuGame import GameDifficulty

    # region Constructor
    def __init__(self, tableSize, regionSize, diff):

        try:
            self._table = SudokuTable(tableSize, regionSize)
        except ValueError as err:
            print(err)
            exit()

        self._Created = 1
        # difficulty setups
        if diff == 1:
            self._gameDifficulty = GameDifficulty.Easy
        elif diff == 2:
            self._gameDifficulty = GameDifficulty.Medium
        elif diff == 3:
            self._gameDifficulty = GameDifficulty.Hard
        else:
            raise ValueError("Bad difficulty level!")
        self.GeneratedFieldCountEasy = 3
        self.GeneratedFieldCountMedium = 4
        self.GeneratedFieldCountHard = 10

    # endregion

    # region Getters from _table
    def GetSize(self):
        return self._table.Size

    def GetRegionSize(self):
        return self._table.RegionSize

    def Table(self):
        return self._table
    # endregion

    # region Game methods
    def IsGameOver(self):
        print(self._table.IsFilled())
        return self._table.IsFilled()

    def NewGame(self, tableSize, regionSize, diff):
        print("--NewGame started--")
        self._table = SudokuTable(tableSize, regionSize)

        # difficulty setups
        if diff == 1:
            self._gameDifficulty = GameDifficulty.Easy
        elif diff == 2:
            self._gameDifficulty = GameDifficulty.Medium
        elif diff == 3:
            self._gameDifficulty = GameDifficulty.Hard
        else:
            raise ValueError("Bad difficulty levels!")

        # difficulty setups
        if self._gameDifficulty == GameDifficulty.Easy:
            self.GenerateStaticFieldsAndDeleteFromIt(
                self.GeneratedFieldCountEasy
            )
        elif self._gameDifficulty == GameDifficulty.Medium:
            self.GenerateStaticFieldsAndDeleteFromIt(
                self.GeneratedFieldCountMedium
            )
        elif self._gameDifficulty == GameDifficulty.Hard:
            self.GenerateStaticFieldsAndDeleteFromIt(
                self.GeneratedFieldCountHard
            )

        self._table._OriginValues = copy.deepcopy(self._table._fieldValues)

    def Fill(self, size):
        start = 0
        iteration = -1
        lastLineStart = 1
        value = 1
        sqrSize = int(sqrt(size))
        for i in range(self._table.Size()):
            iteration = iteration + 1
            if iteration % sqrSize == 0:
                start = start + 1
                value = start
                lastLineStart = value

            else:
                lastLineStart = lastLineStart + sqrSize
                value = lastLineStart

            for j in range(self._table.Size()):
                self._table._fieldValues[i][j] = value
                if value == size:
                    value = 1
                else:
                    value = value + 1

    def ChangeTwoNums(self, size):
        num1 = random.randint(1, size)
        num2 = random.randint(1, size)
        while num2 == num1:
            num2 = random.randint(1, size)

        # two random number change
        for i in range(self._table.Size()):
            for j in range(self._table.Size()):
                if self._table._fieldValues[i][j] == num1:
                    self._table._fieldValues[i][j] = num2
                elif self._table._fieldValues[i][j] == num2:
                    self._table._fieldValues[i][j] = num1

    def IsInGoodIntervall(slef, line1, line2, size):
        sqrtSize = sqrt(size)
        return line1//sqrtSize == line2//sqrtSize

    def ChangeLines(self, size):
        regSize = int(sqrt(size))
        line1 = random.randint(0, size-1)
        line2 = random.randint(0, size-1)
        # check to change good rows only
        while line2 == line1 or self.IsInGoodIntervall(
                line1, line2, size) is False:
            line1 = random.randint(0, size-1)
            line2 = random.randint(0, size-1)

        # chaneg two random rows
        tmp_line = self._table._fieldValues[line1]
        self._table._fieldValues[line1] = self._table._fieldValues[line2]
        self._table._fieldValues[line2] = tmp_line

    def GenerateStaticFieldsAndDeleteFromIt(self, deletecount):
        count = random.randint(1, self._table.Size())
        if self._table.Size() == 4:
            self.Fill(4)
            while count > 0:
                self.ChangeTwoNums(4)
                self.ChangeLines(4)
                count = count - 1
            self.DeleteNums(4, deletecount * 1)  # 3/4/10
        elif self._table.Size() == 9:
            self.Fill(9)
            while count > 0:
                self.ChangeTwoNums(9)
                self.ChangeLines(9)
                count = count - 1
            self.DeleteNums(9, deletecount * 5)  # 15/20/50
        elif self._table.Size() == 16:
            self.Fill(16)
            while count > 0:
                self.ChangeTwoNums(16)
                self.ChangeLines(16)
                count = count - 1
            self.DeleteNums(16, deletecount * 8)  # 24/32/80
        elif self._table.Size() == 25:
            self.Fill(25)
            while count > 0:
                self.ChangeTwoNums(25)
                self.ChangeLines(25)
                count = count - 1
            self.DeleteNums(25, deletecount * 9)  # 27/36/90
        else:
            raise ValueError("ERROR")

    def DeleteNums(self, size, count):
        while count > 0:
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)
            if self._table._fieldValues != 0:
                self._table._fieldValues[x][y] = 0
                count = count - 1
            else:
                count = count + 1

    def GameOver(self, isGameOverP):
        if isGameOverP is True:
            print("GAME OVER!!")
            exit()
    # endregion

    # region Print
    def PrintTableJustNums(self):
        for value in self._table._fieldValues:
            print()
            for item in value:
                if item == 0:
                    print('_, ', end=" ")
                else:
                    print(str(item) + ', ', end=" ")

    def PrintTableWithLetters(self):
        for value in self._table._fieldValues:
            print()
            for item in value:
                if item == 0:
                    print('_, ', end=" ")
                elif item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    print(str(item-1) + ', ', end=" ")
                elif item == 11:
                    print('a, ', end=" ")
                elif item == 12:
                    print('b, ', end=" ")
                elif item == 13:
                    print('c, ', end=" ")
                elif item == 14:
                    print('d, ', end=" ")
                elif item == 15:
                    print('e, ', end=" ")
                elif item == 16:
                    print('f, ', end=" ")
                else:
                    print(str(item) + ", ", end=" ")
        print()

    def PrintTableJustLetters(self):
        for value in self._table._fieldValues:
            print()
            for item in value:
                if item == 0:
                    print('_, ', end=" ")
                elif item == 1:
                    print('A, ', end=" ")
                elif item == 2:
                    print('B, ', end=" ")
                elif item == 3:
                    print('C, ', end=" ")
                elif item == 4:
                    print('D, ', end=" ")
                elif item == 5:
                    print('E, ', end=" ")
                elif item == 6:
                    print('F, ', end=" ")
                elif item == 7:
                    print('G, ', end=" ")
                elif item == 8:
                    print('H, ', end=" ")
                elif item == 9:
                    print('I, ', end=" ")
                elif item == 10:
                    print('J, ', end=" ")
                elif item == 11:
                    print('K, ', end=" ")
                elif item == 12:
                    print('L, ', end=" ")
                elif item == 13:
                    print('M, ', end=" ")
                elif item == 14:
                    print('N, ', end=" ")
                elif item == 15:
                    print('O, ', end=" ")
                elif item == 16:
                    print('P, ', end=" ")
                elif item == 17:
                    print('Q, ', end=" ")
                elif item == 18:
                    print('R, ', end=" ")
                elif item == 19:
                    print('S, ', end=" ")
                elif item == 20:
                    print('T, ', end=" ")
                elif item == 21:
                    print('U, ', end=" ")
                elif item == 22:
                    print('V, ', end=" ")
                elif item == 23:
                    print('W, ', end=" ")
                elif item == 24:
                    print('X, ', end=" ")
                elif item == 25:
                    print('Y, ', end=" ")
                elif item == 26:
                    print('Z, ', end=" ")
                else:
                    print(str(item) + ", ", end=" ")
        print()

    def PrintOriginTable(self):
        for value in self._table._OriginValues:
            print()
            for item in value:
                if item == 0:
                    print('_, ', end=" ")
                else:
                    print(str(item) + ', ', end=" ")
    # endregion

    # region solver
    def CallSolverFromPS(self):
        size = str(len(self._table._fieldValues))
        tableString = ""
        for elem in self._table._fieldValues:
            for value in elem:
                # ',' was not good because of subprocess argument
                tableString = tableString + str(value) + "x"

        # drop last 'x' from end of the string
        tableString = str(tableString[:-1])
        p = subprocess.Popen(
                             ["powershell.exe",
                              r"ps_scripts\solver.ps1 ", size, tableString],
                             stdout=sys.stdout, stderr=sys.stderr)
        print(p.communicate())
    # endregion
