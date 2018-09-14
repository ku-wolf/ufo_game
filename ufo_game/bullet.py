class bullet:
    def __init__(self,x1,x2,y,ang,mx,my,s):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.angle = ang
        self.up = 0
        self.mx = mx
        self.my = my
        self.frame = 0
        self.delay = 3
        self.speed = s
        self.pos = 0
    def shoot(self,speedx):
       if shipx >= -10:
                if self.mx >= self.x1 and self.my >= self.y:
                        self.up += self.speed
                        draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up) - shipx,self.y - toy(2*pi - self.angle,self.up)),4)
                        self.pos = self.x2 + tox(self.angle,self.up)
                elif self.mx <= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up)- shipx,self.y - toy(pi + self.angle,self.up)),4)
                    self.pos = self.x2 + tox(self.angle+pi,self.up)
                elif self.mx <= self.x1 and self.my <= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(pi -self.angle,self.up)- shipx,self.y - toy(self.angle,self.up)),4)
                    self.pos =self.x2 + tox(pi -self.angle,self.up)
                elif self.mx >= self.x1 and self.my <= self.y:
                    self.up +=  self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up)- shipx,self.y - toy(self.angle,self.up)),4)
                    self.pos =self.x2 + tox(self.angle,self.up)
       if shipx < -10:
            if self.mx >= self.x2 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x2  and self.my >= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x2  and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(pi-self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x2 and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
    def shipshoot(self,speedx):
        if self.x1 == 424:

            if self.mx >= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    self.x2 -= speedx
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x1 and self.my >= self.y:
                self.up += self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x1 and self.my <= self.y:
                self.up += self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(pi -self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x1 and self.my <= self.y:
                self.up +=  self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
        if self.x1 < 424:

            if self.mx >= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x1  and self.my >= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x1  and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(pi-self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x1 and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
    def animate(self):
                self.delay -= 1                         # count down to zero
                if self.delay == 0:                     # then advance frame like normal
                    self.delay = 20
                    self.frame += 1
                    if self.frame == 9:
                        self.frame = 0