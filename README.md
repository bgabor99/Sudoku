# Sudoku
## Sudoku game in python with powershell solver
### How to play?
- Run
```python
python3 program.py
```
- It has a simple cmd menu where you can navigate through the game options
    - Difficulty can be Easy/Medium/Hard
        - The harder the game, the more empty spaces there will be
    - Table size can be 4/9/16/25
---
- SudokuGame.py: It's represents a game
- SudokuTable.py: It's represents a table (int matrix)
- ps_scripts/solver.py: It's solves the generated sudoku, called as a subprocess
