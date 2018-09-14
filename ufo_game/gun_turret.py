class badgun:
    def __init__(self,x,y,ang):
        self.x = x
        self.y = y
        self.l = 50
        self.w = 20
        self.rect =Rect(x,y,20,50)
        self.listpos = []
        self.listshots = []
        self.delay = 0
        self.rate = randint(50,1000)
        self.health = 100
        self.angle = ang
    def shoot(self, shipx):
        if shipx >= -10:
                self.angle = getangle(distance(self.x-shipx+10,self.y,self.x-shipx+10,shipy),distance(self.x-shipx+10,self.y,424,self.y))
        elif shipx < -10:
                self.angle  = getangle(distance(self.x+10,self.y,self.x+10,shipy),distance(self.x+10,self.y,shipx+424,self.y))
        if self.delay == 0:
            if shipx >= -10:
                ang = getangle(distance(self.x-shipx+10,self.y,self.x-shipx+10,shipy),distance(self.x-shipx+10,self.y,424,self.y))
                self.listshots.append(bullet(self.x+10-shipx,self.x,self.y,ang,424,shipy,10))
                self.delay +=1
            elif shipx < -10:
                ang  = getangle(distance(self.x+10,self.y,self.x+10,shipy),distance(self.x+10,self.y,shipx+424,self.y))
                self.listshots.append(bullet(self.x+10,self.x+10,self.y,ang,shipx+424,shipy,10))
                self.delay +=1
        else:
            self.delay +=1
            if self.delay == self.rate:
                self.delay = 0