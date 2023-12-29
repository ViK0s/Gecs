

import numpy as np
import math
import os
#overwrite pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

#Physical constants
g = 6.647 * 10**(-11)
k = 8.987511 * 10**9

class circle:
    def __init__(self, xc, yc, r, color):
        self.xc=xc
        self.yc=yc
        self.color=color
        self.r = r
    def draw(self,window):
        pygame.draw.circle(window, self.color,#np:(0,   0, 255) or "blue",
        [self.xc, self.yc], self.r#no outline
        )



class massObject(circle):
    def __init__(self,xc,yc, r, color, mass = 0, q = 0, v = list([0,0])):
        self.r=r
        self.xc=xc
        self.yc=yc
        self.color = color
        self.mass = mass
        self.v = v
        self.q = q
        
        circle.__init__(self,xc,yc,self.r,color)
    #Change the input, to be an obj list, not a single obj!
    def SimulateGravity(self, obj):
        templst = [self.xc, self.yc]
        templst2 = [obj.xc, obj.yc]
        vctr = np.array(templst)
        vctrobj = np.array(templst2)
        mag = np.linalg.norm(vctrobj-vctr)
        
        self.a = g*(obj.mass/((mag)**3))*((vctrobj-vctr))
        self.v += self.a
        #scaling of v
        if self.v[0] >= 3 or self.v[1] >= 3: 
            self.v *= 0.5
        
        
        self.xc += self.v[0]
        self.yc += self.v[1]
    #Accepts vector of type string : 
        #"v", "a", etc.
    def DrawVector(self, vector, scale, window):
        #Checking which vector to use
        #There's better ways of doing this, passing a value is infinitley much better, and more readable than this, methods can just return values which can be used
        #example, simgrav can return whichever value the user needed by calling another arg into it that can be checked, simelectric doesnt need that arg, which is even better
        if vector == "v":
            vector = self.v
        elif vector == "a":
            vector = self.a 
        elif vector == "E":
            #if self.q != None:
                vector = self.E
            #else:
            #    print("bad args")
            #    return
        
        scaledVector = vector * scale
        #Choose the ending position of vector
        #WARNING, the numpy vector is made into a list here!!!!
        scaledVectorEnd = [scaledVector[0]+self.xc, scaledVector[1]+self.yc]
        
        #draw vector
        pygame.draw.line(window,"green",[self.xc, self.yc],scaledVectorEnd,2)
        rotation = math.degrees(math.atan2([self.xc, self.yc][1]-scaledVectorEnd[1], scaledVectorEnd[0]-[self.xc, self.yc][0]))+90
        pygame.draw.polygon(window, "green", ((scaledVectorEnd[0]+5*math.sin(math.radians(rotation)), scaledVectorEnd[1]+5*math.cos(math.radians(rotation))), (scaledVectorEnd[0]+5*math.sin(math.radians(rotation-120)), scaledVectorEnd[1]+5*math.cos(math.radians(rotation-120))), (scaledVectorEnd[0]+5*math.sin(math.radians(rotation+120)), scaledVectorEnd[1]+5*math.cos(math.radians(rotation+120)))))
    def SimElectricField(self, objlist):
        self.E = 0
        for obj in objlist:
            templst = [self.xc, self.yc]
            templst2 = [obj.xc, obj.yc]
            vctr = np.array(templst)
            vctrobj = np.array(templst2)
            mag = np.linalg.norm(vctr-vctrobj)
            etemp = (obj.q/(mag**2))*(vctr-vctrobj)
            self.E += etemp
        self.E *= k


#position : list of list
#amount : int
#mass : list
#speed : list of list
#color : list
#q : list

def ObjSpawn(position:list, amount:int, mass, color, q, speed):
    objlist = []
    for i in range(amount):
        #temp var, change name please
        xc = int(position[i][0])
        yc = int(position[i][1])
        if mass == 0:
            mass = [0] * amount
        if color == 0:
            color = ["black"] * amount
        if q == 0:
            q = [0] * amount
        if speed == 0:
            speed = [[0, 0]] * amount
        objlist.append(massObject(xc, yc, 5, color[i], int(mass[i]),int(q[i]), ConvertListTypeToInt(speed[i])) )
    return objlist
def ObjSim(objlist, window, check):
    for i in objlist:
        i.draw(window)
        i.DrawVector("v", 100, window)
        
        if check == "g":
            for n in range(len(objlist)):
                if objlist[n] != i:
                    i.SimulateGravity(objlist[n])
        #elif check == "e":
        #    i.SimElectricField(objlist)
#functions below this could really use their own module
#this function splits the string fed into it and makes a list.
def SplitStringIntoList(string):
    li = list(string.split(" "))
    return li
#rename, makes a list of lists from a list
def afterConvert(list):
    pa = []
    templist = []
    for n in list:
        templist = list[:2]
        list.pop(0)
        list.pop(0)
        pa.append(templist) 
    return pa
#Converts args inside list into int
def ConvertListTypeToInt(list):
    templist = []
    for i in range(len(list)):
        templist.append(int(list[i]))
    return templist    


