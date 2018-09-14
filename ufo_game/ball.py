class ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vydown = 0
        self.vyup = 0
        self.speed =  randint(1,2)
        self.destx = self.speed *(randint(0,10000/self.speed))
        self.wieght = 5
        self.col = 255,0,0
        self.pic = charpics
        self.captured = False
    def move(self):
        if shipx >= -10 and shipx <= 9149:
                if mb[2] == 1  and  self.y > shipy and self.x-192/4-shipx >= 424-dist/5 and self.x-192/4-shipx <= 424+dist/5:
                    self.vydown = 0
                    self.vyup += int(500/dist)
                    self.y -= - self.wieght + self.vyup
                    self.vx = speedx
                    if self.x-shipx-192/6 > 424:
                        self.x -= 3
                    if self.x-shipx-192/6 < 424:
                        self.x += 3
                elif self.y < 575 and -self.wieght + self.vyup <= 0:
                    self.vyup -= 1
                    self.vydown += 1
                    self.y += self.wieght + self.vydown - self.vyup
                    self.x += self.vx
                elif self.y < 575:
                        self.vyup -= 1
                        self.vydown += 1
                        self.y += self.wieght + self.vydown - self.vyup
                        self.x += self.vx
                elif self.y == 575:
                    self.vydown = 0
                    self.vx = 0
                    if self.destx == self.x:
                        self.destx =  randint(0,799)
                    else:
                        if self.destx < self.x:
                            self.x -= self. speed+self.vx
                        if self.destx > self.x:
                            self.x += self.speed+self.vx
                if self.y >575:
                    self.y = 575
        if shipx < -10:
                if mb[2] == 1  and  self.y > shipy and self.x-192/4 >= shipx+424-dist/5 and self.x-192/4 <= shipx+424+dist/5:
                    self.vydown = 0
                    self.vyup += int(500/dist)
                    self.y -= - self.wieght + self.vyup
                    self.vx = speedx
                    if self.x - 192/6 > shipx + 424:
                        self.x -= 2
                    if self.x - 192/6 < shipx + 424:
                        self.x += 2
                elif self.y < 575 and -self.wieght + self.vyup <= 0:
                    self.vyup -= 1
                    self.vydown += 1
                    self.y += self.wieght + self.vydown - self.vyup
                    self.x += self.vx
                elif self.y < 575:
                        self.vyup -= 1
                        self.vydown += 1
                        self.y += self.wieght + self.vydown - self.vyup
                        self.x += self.vx
                elif self.y == 575:
                    self.vydown = 0
                    self.vx = 0
                    if self.destx == self.x:
                        self.destx =  randint(15,799)
                    else:
                        if self.destx < self.x:

                            self.x -= self.speed+self.vx
                        if self.destx > self.x:
                            self.x += self.speed+self.vx
                if self.y >575:
                    self.y = 575