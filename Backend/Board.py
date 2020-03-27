#################################################
#   Board Creation
# 5x5


# Outside the Board Class there is going to be a
# Game class that has the board and the overal score

# Create Board Class
## Create Board a board with 5x5 words
## Each word has position(x,y), state (clicked/unclicked) Type
## The board has the remaining spyies. 
## Board changes the Words state
## 1. approach to create the board is create a dictionary with the position and its respective values

import random 


class Word():

    def __init__(self, x, y, word):
        self.X = x
        self.Y = y
        self.Word = word
        self.Clicked = False
        self.Type = None

class Board():
    WORD_LIST = [ "Python", "Ruby", "Java", "C#", "C", \
                  "Go", "Javascript", "React", "Angular", "C++", \
                  "Vue", "Typescript", "Jquery", "Flask", "Node" \
                  "SQL", ".Net", "Oracle", "MySQL", "IIS", \
                  "Django", "Celery", "Express", "MVC", "Docker", "Travis"]
    ROWS = 5
    COLUMNS = 5

    def __init__(self):
        self.Words = {}
        
    def CreateNewBoard(self):
        temp = self.WORD_LIST.copy()
        for r in range(0, self.ROWS):
            for c in range(0,self.COLUMNS):
                end = len(temp) - 1
                pull = temp.pop(random.randint(0, end))
                self.Words.update({(r,c): Word(r,c,pull)})
    
    def AssigneTypesToWords(self):
        


if __name__ == "__main__":
    board = Board()

    board.CreateNewBoard()