import SimulationCore as SimC
import pygame
import sys
input = sys.argv
#position : list of list
#amount : int
#mass : list
#speed : list of list
#color : list
def ObjSpawn(position, amount, mass, color, speed):
    objlist = []
    for i in range(amount):
        #temp var, change name please
        xc = int(position[i-1][0])
        yc = int(position[i-1][1])
        objlist.append(SimC.massObject(xc, yc, 5, color[i-1], int(mass[i-1]),0, ConvertListTypeToInt(speed[i-1])) )
    return objlist
def ObjSim(objlist):
    for i in objlist:
        i.draw(screen)
        i.DrawVector("v", 100, screen)
        
        for n in range(len(objlist)):
            if objlist[n] != i:
                i.SimulateGravity(objlist[n])
#rename, this function splits the string fed into it and makes a list.
def Convert(string):
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

    
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
#objekt = SimC.massObject(680, 320, 5, "blue", 20000000000000, [0,0])
#objekt2 = SimC.massObject(100, 200, 5, "red", 1000000000000,[1,-1])
firstinptemp = afterConvert(Convert(input[1]))
lol = Convert(input[3])

#print(type(lol))
x = ObjSpawn(firstinptemp, 2, ConvertListTypeToInt(lol), Convert(input[2]), afterConvert(Convert(input[4])))

while running:
    screen.fill("white")
    #objekt.draw(screen)
    #objekt2.draw(screen)
    ObjSim(x)
    #x[0].draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #objekt.SimulateGravity(objekt2, dt)
    #objekt2.SimulateGravity(objekt, dt)
    #objekt.DrawVector("v", 100, screen)
    #object position debugging
    """font = pygame.font.Font(None, 64)
    #text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " v: " + str(round(objekt.v[0], 2))+ " " + str(round(objekt.v[1], 2)), True, (10, 10, 10))
    text = font.render(firstinptemp, True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging"""
    pygame.display.flip()
pygame.quit()