import random

board = []
count = 0
allNum_set = set()

for row in range(10):
    board.append([])
    for column in range(10):
        # Assign x to each row
        x = random.randint(0,99)
        board[row].append(str(x).zfill(2))
        allNum_set.add(x)

def get_location(number):
    for row in range(10):
        for column in range(10):
            if board[row][column] == str(number):
                return [row+1, column+1]

# Find the first four largest numbers and their locations on the board                    
allNum_set = sorted(allNum_set, reverse=True)
firstLargestNum = allNum_set[0]
firstLargestNumLoc = get_location(firstLargestNum)
secondLargestNum = allNum_set[1]
secondLargestNumLoc = get_location(secondLargestNum)
thirdLargestNum = allNum_set[2]
thirdLargestNumLoc = get_location(thirdLargestNum)
fourthLargestNum = allNum_set[3]
fourthLargestNumLoc = get_location(fourthLargestNum)

# Function will print board like an actual board
def print_space(board):
    for row in board:
        print (" ".join(row))

print_space(board)
print()
print("The first highest number is {0} at {1}, the second is {2} at {3},\n\
the third is {4} at {5}, and the fourth is {6} at {7}"
      .format(str(firstLargestNum), firstLargestNumLoc, str(secondLargestNum),
      secondLargestNumLoc, str(thirdLargestNum), thirdLargestNumLoc,
      str(fourthLargestNum), fourthLargestNumLoc))