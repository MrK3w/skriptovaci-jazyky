import playground
import random
import sys

class Atom(object):
    def __init__(self, pos_x, pos_y, rad, color,speed_x,speed_y):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.rad = float(rad)
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self, width, height):
        self.check_position(width,height)
        if (self.pos_x) + self.speed_y >= height-self.rad:
            self.pos_y = height-self.rad
        else:
            self.pos_y = self.pos_y + self.speed_y
        if (self.pos_x-self.rad) + self.speed_x > width-self.rad:
            self.pos_x = width-self.rad
            self.speed_x *= -1
        else:
            self.pos_x = self.pos_x + self.speed_x

    def check_position(self,width,height):
        tmp_pos_x =self.pos_x + self.speed_x
        tmp_pos_y =self.pos_y + self.speed_y
        if tmp_pos_x < 0 or tmp_pos_x >= width:
            self.speed_x *= -1
        if tmp_pos_y < 0 or tmp_pos_y >= height:
            self.speed_y *= -1

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.rad, self.color)
        

class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.width = width
        self.height = height
        self.atoms = []
        for i in range(0,count):
            self.atoms.append(self.random_atom())
        #self.atoms.append(Atom(120, 160, 20, 'green'))

    def random_atom(self):
        color = random.choice([enm.value for enm in playground.Colors])
        generate = random.randint(0,1)
        if generate == 0:
            return FallDownAtom(random.randint(0+50,self.size_x-50),random.randint(0+50,self.size_y-50),random.randint(5,15),color,random.randint(1,5),random.randint(5,15))
        elif generate == 1:
            return Atom(random.randint(0+50,self.size_x-50),random.randint(0+50,self.size_y-50),random.randint(5,15),'white',random.randint(1,5),random.randint(5,15))

        
    def tick(self, size_x, size_y):
        self.height = size_y
        self.width = size_x
        ret = []
        for atom in self.atoms:
            atom.move(self.width,self.height)
            ret.append(atom.to_tuple())
        return tuple(ret)

class FallDownAtom(Atom):
    def __init__(self,pos_x, pos_y, rad, color,speed_x,speed_y):
        super().__init__(pos_x, pos_y, rad, color,speed_x,speed_y)
        self.g = 3
        self.damping = 0.8
    
    def move(self,width,height):
        self.check_position(width,height)
        self.speed_y += self.g
        if (self.pos_y+self.rad) + self.speed_y >= height-self.rad:
            self.pos_y = height-self.rad
            self.speed_y *= self.damping
            self.speed_x *= self.damping
        else:
            self.pos_y = self.pos_y + self.speed_y
        if (self.pos_x-self.rad) + self.speed_x > width-self.rad:
            self.pos_x = width-self.rad
            self.speed_x *= -1
        else:
            self.pos_x = self.pos_x + self.speed_x
       

    def check_position(self,width,height):
        tmp_pos_x =self.pos_x + self.speed_x
        tmp_pos_y =self.pos_y + self.speed_y
        if tmp_pos_x >= width-self.rad:
            self.speed_x *= -1
        if tmp_pos_x < 0:
            self.speed_x *= -1
        if tmp_pos_y < 0 or tmp_pos_y > height:
            self.speed_y *= -1


if __name__ == '__main__':
    size_x, size_y = 400, 300
    world = ExampleWorld(10, size_x, size_y)
    playground.run((size_x, size_y), world)
