"""
    ---------- Tower of Hanoi Problem ----------
    Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
    The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack 
        i.e. a disk can only be moved if it is the uppermost disk on a stack.
    3. No disk may be placed on top of a smaller disk.
    
    Solution:
    Move n disk from from_rod to to_rod by -
    1. moving n-1 disk from from_rod to aux_rod
    2. move nth disk from from_rod to to_rod
    3. moving n-1 from aux_rod to to_rod
"""


def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("n Move disk 1 from rod %s to rod %s" % (from_rod, to_rod))
        return

    tower_of_hanoi(n-1, from_rod=from_rod, to_rod=aux_rod, aux_rod=to_rod)
    print("n Move disk %d from rod %s to rod %s" % (n, from_rod, to_rod))
    tower_of_hanoi(n-1, from_rod=aux_rod, to_rod=to_rod, aux_rod=from_rod)

if __name__ == '__main__':
    tower_of_hanoi(10, "A", "B", "C")
