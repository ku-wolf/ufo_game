class buildings:
    def __init__(self,x,y):
        self.x =x
        self.y =y
        self.l = 120
        self.w = 60
        self.rect = Rect(x,y,60,120)
        self.timer = 0
    def createguys(self,shipx):
        if self.timer == 0:
            balls.append(ball(self.x+75,575))
            self.timer +=1
        else:
            self.timer +=1
            if self.timer == 10:
                self.timer = 0