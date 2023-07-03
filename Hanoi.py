# TASK:
#
# Please read: https://en.wikipedia.org/wiki/Tower_of_Hanoi

# disks stacked on one rod in order of decreasing size, the smallest at the top
Towers = [[5, 4, 3, 2, 1],
    [],
    []
]

# The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
#
# 1. Only one disk may be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a disk that is smaller than it.

# please implement function to solve to puzzle

def solve_puzzle():
    print("Hanoi towers",Towers)
    move_from_where = int(input("Where from: "))
    move_what= int(input("What to move: "))
    move_to_where= int(input("Where to move: "))

    if len(Towers[move_from_where])==0:
        print("nothing to move")
        return False
    if move_what!=min(Towers[move_from_where]):
        print("You cant move that circle")
        return False

    elif len(Towers[move_to_where])==0:
        Towers[move_to_where].append(move_what)
        Towers[move_from_where].remove(move_what)

    elif move_what<(min(Towers[move_to_where])):
        Towers[move_to_where].append(move_what)
        Towers[move_from_where].remove(move_what)
    else:
        print("You cant move there")
        return False
    if Towers[2]==[5, 4, 3, 2, 1]:
        print("You have won")
        return True
while True:
    solve_puzzle()