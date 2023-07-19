class SudokuTable:

    # region Constructor
    def __init__(self, tableSize, regionSize):
        if tableSize in [4, 9, 16, 25]:
            print("Table size is: ", tableSize)
        else:
            raise ValueError("Bad tableSize and regionSize")

        self._regionSize = regionSize
        self._tableSize = tableSize
        self._fieldValues = []
        for _ in range(tableSize):
            self._fieldValues.append([0]*tableSize)

        self._OriginValues = []
        for _ in range(tableSize):
            self._OriginValues.append([0]*tableSize)
    # endregion

    # region Table methods
    def IsFilled(self):
        for value in self._fieldValues:
            for item in value:
                if item == 0:
                    return False
        return True

    def RegionSize(self):
        return self._regionSize

    def Size(self):
        return int(len(self._fieldValues))

    def IsEmpty(self, x, y):
        if x < 0 or x >= len(self._fieldValues):
            raise ValueError("The X coordinate is out of range")
        if y < 0 or y >= len(self._fieldValues):
            raise ValueError("The Y coordinate is out of range")

        return self._fieldValues[x][y] == 0

    def GetValue(self, x, y):
        if x < 0 or x >= len(self._fieldValues):
            raise ValueError("The X coordinate is out of range")
        if y < 0 or y >= len(self._fieldValues):
            raise ValueError("The Y coordinate is out of range")
        return self._fieldValues[x][y]
    # endregion
