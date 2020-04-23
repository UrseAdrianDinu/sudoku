import pygame
import random
from random import randint
from rezolva import solve, valid
import time
pygame.font.init()
class Grid:
    b0=[
        [0, 0, 0 ,0, 0, 0, 6, 0, 9],
        [1, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 5, 3, 0, 6, 8, 2, 1],
        [0, 0, 4, 6, 7, 0, 0, 5, 0],
        [0, 0, 7, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 5, 4, 0, 0, 0, 0],
        [3, 7, 0, 4, 0, 5, 2, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 1, 0],
        [0, 6, 0, 0, 2, 0, 0, 3, 7]
    ]
    
    b1= [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    
    b2= [
        [0, 6, 8 ,0, 0, 0, 9, 3, 0],
        [0, 4, 2, 0, 0, 0, 6, 0, 0],
        [1, 9, 0, 0, 8, 0, 0, 4, 0],
        [0, 8, 5, 2, 0, 1, 0, 0, 7],
        [7, 0, 0, 8, 9, 0, 0, 0, 0],
        [2, 0, 9, 0, 0, 7, 5, 0, 3],
        [0, 2, 0, 1, 0, 0, 0, 5, 0],
        [8, 5, 0, 0, 4, 0, 7, 6, 0],
        [4, 7, 3, 0, 5, 2, 0, 0, 9]
    ]
    
    b3=[
        [0, 0, 0 ,4, 0, 0, 2, 0, 0],
        [0, 4, 2, 0, 0, 0, 0, 1, 8],
        [5, 0, 6, 9, 0, 0, 0, 3, 0],
        [0, 6, 9, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 2, 1],
        [8, 0, 0, 1, 5, 7, 6, 0, 9],
        [0, 0, 0, 0, 3, 0, 9, 6, 0],
        [9, 0, 0, 6, 0, 2, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 2]
    ]
   
    b4=[
        [0, 0, 6 ,0, 3, 1, 0, 7, 0],
        [4, 3, 7, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 4, 6, 7, 0, 0, 8],
        [0, 2, 9, 1, 7, 8, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 6],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 5, 0, 0, 4, 9, 1, 0],
        [0, 0, 3, 5, 0, 9, 0, 8, 7],
        [7, 9, 0, 0, 8, 6, 0, 0, 4]
    ]
    
      
    b5=[
        [2, 5, 0 ,0, 0, 3, 0, 9, 1],
        [3, 0, 9, 0, 0, 0, 7, 2, 0],
        [0, 0, 1, 0, 0, 6, 3, 0, 0],
        [0, 0, 0, 0, 6, 8, 0, 0, 3],
        [0, 1, 0, 0, 4, 0, 0, 0, 0],
        [6, 0, 3, 0, 0, 0, 0, 5, 0],
        [1, 3, 2, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [7, 6, 4, 0, 1, 0, 0, 0, 0]
    ]
    
      
    b6=[
        [9, 1, 7 ,2, 5, 4, 0, 0, 0],
        [4, 0, 2, 0, 8, 0, 0, 0, 0],
        [6, 5, 0, 0, 0, 3, 4, 0, 0],
        [0, 0, 3, 0, 9, 0, 2, 5, 6],
        [5, 0, 0, 7, 0, 0, 3, 0, 9],
        [2, 0, 0, 0, 0, 5, 0, 7, 1],
        [0, 2, 0, 5, 3, 0, 7, 6, 0],
        [3, 7, 0, 1, 6, 0, 0, 9, 8],
        [0, 0, 0, 0, 0, 0, 0, 3, 0]
    ]
    
    b7=[
        [1, 5, 0 ,0, 4, 2, 0, 0, 6],
        [2, 7, 4, 5, 6, 0, 0, 1, 0],
        [0, 0, 6, 0, 0, 7, 4, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 6, 0, 4, 0, 3, 1, 9, 0],
        [0, 2, 0, 6, 0, 5, 9, 0, 0],
        [9, 8, 5, 0, 3, 0, 0, 6, 0],
        [0, 4, 0, 2, 1, 9, 8, 3, 0]
    ]
    
    b8=[
        [0, 3, 1 ,6, 0, 7, 0, 0, 0],
        [6, 0, 0, 8, 0, 0, 2, 5, 7],
        [8, 0, 0, 0, 9, 0, 6, 0, 3],
        [4, 0, 0, 0, 0, 0, 8, 3, 2],
        [0, 1, 0, 0, 6, 9, 0, 0, 0],
        [7, 0, 3, 2, 4, 0, 0, 0, 6],
        [9, 0, 2, 4, 0, 1, 0, 7, 8],
        [0, 8, 5, 0, 0, 0, 0, 0, 9],
        [3, 0, 4, 0, 0, 0, 0, 6, 1]
    ]
    
    b9=[
        [0, 6, 0 ,0, 8, 0, 4, 2, 0],
        [0, 1, 5, 0, 6, 0, 3, 7, 8],
        [0, 0, 0, 4, 0, 0, 0, 6, 0],
        [1, 0, 0, 6, 0, 4, 8, 3, 0],
        [3, 0, 6, 0, 1, 0, 7, 0, 5],
        [0, 8, 0, 3, 5, 0, 0, 0, 0],
        [8, 3, 0, 9, 4, 0, 0, 0, 0],
        [0, 7, 2, 1, 3, 0, 9, 0, 0],
        [0, 0, 9, 0, 2, 0, 6, 1, 0]
    ]
    
    
    b=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9]  #o lista de board-uri
    a=random.randint(0,10)              
    print(a)
    board=b[a]                          #selecteaza random un board
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)] #ficarei celule ii este atribuita valoarea
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)] #face update la valorile din board
        #print(self.model)

    def place(self, val):
        row, col = self.selected #luam coord celulei 
        if self.cubes[row][col].value == 0:   #verificam daca celula este libera
            self.cubes[row][col].set(val)     #seteaza valoarea
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):  #verificam daca valoarea introdusa e buna
                return True
            else:
                self.cubes[row][col].set(0)      #daca nu e buna valoarea, celula ramane goala
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):          #seteaza valoarea temporara
        row, col = self.selected     
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # deseneam liniile tablei
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # desenam valorile celulei
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)   #setam coord celulei alese

    def clear(self):  #folosita pentru butonul de stergere
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):  #returneaza coord celulei alese cu ajutorul mouse-ului
        #pos[0]=row si pos[1]=col
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self): #verificam daca tabla a fost completata in totalitate
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value  #nu mai poate fi modificata
        self.temp = 0       #valoare temporara folosita pentru a introduce de la tastura dar care poate fi modificata inaintea apasarii tastei enter
        self.row = row      #9
        self.col = col      #9
        self.width = width    #folosite pentru dimensiunea ferestrei
        self.height = height
        self.selected = False  #folosit atunci cand este selectata o celula

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans",30)  #definirea font-ului

        gap = self.width / 9     #dimensiunea unei celule
        x = self.col * gap       
        y = self.row * gap

        if self.temp != 0 and self.value == 0:              #verifica daca val introdusa e diferita de 0 si daca celula este libera
            text = fnt.render(str(self.temp), 1, (0,0,255))  #daca da, scrie valoarea in celula
            win.blit(text, (x+25, y+20))
        elif not(self.value == 0):                          #daca celula este deja ocupata, pastreaza valoarea initiala din casuta
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:                                   #folosit pentru a selecta o celula
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):  
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board, strikes):  #functie folosita pentru a face update board-ului
    win.fill((255,255,255))
    fnt = pygame.font.SysFont("comicsans", 30)
    # x-uri
    text = fnt.render("X " * strikes, 1, (255, 0, 0)) 
    win.blit(text, (20, 560))       #deseneaza x-urile
    # deseneaza board-ul
    board.draw(win)



def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    strikes = 0
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #buton de x
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp): 
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None
                        if strikes==3:   #daca s-au facut 3 greseli, jocul se termina
                            win.fill((255,255,255))
                            pygame.display.update()
                            LARGEFONTSIZE = 70
                            LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)
                            aaa=LARGEFONT.render("YOU LOST :(", True, (255,0,0))
                            c = aaa.get_rect()
                            c.topleft = (70, 300)
                            win.blit(aaa, c)
                            pygame.display.update()
                            
                            pygame.time.wait(4000)
                            
                            run=False
                        if board.is_finished():  #jocul se termina daca au fost facute mai putin de 3 greseli si tabla e completata
                            win.fill((255,255,255))
                            pygame.display.update()
                            LARGEFONTSIZE = 70
                            LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)
                            aaa=LARGEFONT.render("YOU WIN :)", True, (0,255,0))
                            c = aaa.get_rect()
                            c.topleft = (70, 300)
                            win.blit(aaa, c)
                            pygame.display.update()
                            
                            pygame.time.wait(4000)
                            
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:  #selectam celula cu ajutorul mouse-ului
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, strikes)
        pygame.display.update()


main()
pygame.quit()