import pygame
from MainFrame import MainFrame

class GUI :

    def __init__(self,row,column):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800), 0, 32)
        self.frame = MainFrame(row, column)
        self.positions = [[0 for i in range(column)] for j in range(row) ]
        self.COUNT = pygame.USEREVENT + 1

        pygame.time.set_timer(self.COUNT, 500)  #Time
        pygame.display.set_caption("LifeGame")  # 标题
        self.screen.fill((200, 200, 200))

        for i in range(self.frame.Row):
            for j in range(self.frame.Column):
                x = i*600/self.frame.Row
                y = j*600/self.frame.Column
                self.positions[i][j] = (x,y+200)
        pygame.draw.rect(self.screen, (255, 255, 255),((5,5), (140, 50)))
        pygame.draw.rect(self.screen, (255, 255, 255),((155,5), (140, 50)))
        pygame.draw.rect(self.screen, (255, 255, 255), ((305, 5), (140, 50)))
        pygame.draw.rect(self.screen, (255, 255, 255), ((455, 5), (140, 50)))
        self.screen.blit(self.drawText("start"), (50, 20))
        self.screen.blit(self.drawText("pause"), (200, 20))
        self.screen.blit(self.drawText("reset"), (350, 20))
        self.screen.blit(self.drawText("random"), (490, 20))

    def drawText(self,content):
        pygame.font.init()
        font = pygame.font.Font(None, 30)
        text_sf = font.render(content, True, pygame.Color(0, 0, 0), pygame.Color(255, 255, 255))
        return text_sf


    def show(self):
        for i in range(self.frame.Row):
            for j in range(self.frame.Column):
                if self.frame.GameMap[i][j] == 1 :
                    pygame.draw.rect(self.screen, (0, 0, 0), (self.positions[i][j], (600 // self.frame.Row - 5, 600 // self.frame.Column - 5)))
                elif self.frame.GameMap[i][j] == 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (self.positions[i][j], (600 // self.frame.Row - 5, 600 // self.frame.Column - 5)))

        pygame.display.update()


    def random_init(self):
        self.frame.random_init()
        self.show()

    def start(self):
        self.frame.GameStatus = 1
        return self.frame.GameStatus

    def pause(self):
        self.frame.GameStatus = 0
        return self.frame.GameStatus

    def reset(self):
        self.frame.reset()
        self.show()

    def mainloop(self):
        pygame.display.flip()
        self.show()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.frame.GameStatus==0:
                        if event.pos[1]<=55:
                            t = event.pos[0]//150
                            if t==0 :
                                self.start()
                            elif t==2 :
                                self.reset()
                            elif t==3 :
                                self.random_init()
                            continue

                        for i in range(len(self.positions)):
                            for j in range(len(self.positions[i])):
                                rec = self.positions[i][j]
                                if event.pos[0] >= rec[0] and event.pos[0] <= (rec[0] + 600 // self.frame.Row - 5) and event.pos[1] >= rec[1] and event.pos[1] <= (rec[1] + 600 // self.frame.Row - 5) :
                                    self.frame.GameMap[i][j] = 1^self.frame.GameMap[i][j]
                                    self.show()
                                    break
                    else :
                        if event.pos[1]<=55:
                            t = event.pos[0]//150
                            print(event.pos)
                            print(t)
                            if t==1 :
                                self.pause()

                elif event.type == self.COUNT:
                    if self.frame.GameStatus == 1:
                        self.frame.next_phrase()
                        self.show()











if __name__ == '__main__' :
    gui = GUI(30,30)
    gui.random_init()
    gui.mainloop()




           # print(event.pos)
