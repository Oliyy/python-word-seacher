def get_name():
    return "423542626|Oliy_Barrett"

def print_puzzle(Puzzle):
    for x in Puzzle:
        print(x)

def load_words_to_find(file_name):
    file = open(file_name, "r")
    word_list = []
    for line in file:
        word_to_insert = line.rstrip('\n') # Removes \n from all words in the array
        word_list.append(word_to_insert)
    return word_list

def find_horizontal(Puzzle,Words,ReplaceWith):
    Found = []
    i = 0
    n = 0
    while i < len(Puzzle):
        while n < len(Words)-1: # There is some extra spoopy line lol
            n += 1
            if Words[n] in Puzzle[i]:
                print("!")
                # Puzzle[i].replace(Words[n], "yes")
                Found.append(Words[n])
        n = 0
        i += 1
    ReversePuzzle = []
    for x in Puzzle:
        ReversePuzzle.append(x[::-1])
    q = 0
    w = 0
    while q < len(ReversePuzzle):
        while w < len(Words)-1: # There is some extra spoopy line lol
            w += 1
            if Words[w] in ReversePuzzle[q]:
                print(Words[w])
                # Puzzle[q].replace(Words[w], "yes")
                Found.append(Words[w])
        w = 0
        q += 1
    print(Found)
    OutPuz = Puzzle
    return(OutPuz, Found)

def rotate_puzzle(Puzzle):
    RotatePuz = Puzzle[2:]+Puzzle[:2]
    NewPuzzle = []
    for x in Puzzle:
        NewPuzzle.append(x[::-1])
    print(NewPuzzle)
    print(RotatePuz)
    return RotatePuz

# def find_vertical(Puzzle,Words):

if __name__ == '__main__':

    Puzzle = ["FUNCTIONRRIRAI",
             "RAIOONFRCCPWON",
             "PTCSNOBEUITOLO",
             "BNCACIANTOSLIH",
             "RBYOLILYNREFBT",
             "HYYNOGESTIBRIY",
             "AATTSIONCMCENP",
             "UORTENRRCBFVAU",
             "CEBEECVWIERORI",
             "PROCESSORTOPYF",
             "OHCOMPUTERHSOS",
             "YCYPRESREOSMRW",
             "OATHBRMVTHHCTR",
             "PGORWOOUIPSCHP"]

Words = load_words_to_find("words.txt")
# print_puzzle(Puzzle)
find_horizontal(Puzzle,Words,".")
rotate_puzzle(Puzzle)
