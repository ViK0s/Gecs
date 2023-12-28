import SimulationCore as SimC
import pygame
import sys
input = sys.argv
#position : list of list
#amount : int
#mass : list
#speed : list of list
#color : list
#q : list

    
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
#objekt = SimC.massObject(680, 320, 5, "blue", 20000000000000, [0,0])
#objekt2 = SimC.massObject(100, 200, 5, "red", 1000000000000,[1,-1])
firstinptemp = SimC.afterConvert(SimC.SplitStringIntoList(input[1]))
lol = SimC.SplitStringIntoList(input[3])

#print(type(lol))
x = SimC.ObjSpawn(firstinptemp, 2, SimC.ConvertListTypeToInt(lol), SimC.SplitStringIntoList(input[2]),0, SimC.afterConvert(SimC.SplitStringIntoList(input[4])))

while running:
    screen.fill("white")
    SimC.ObjSim(x, screen, "g")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """font = pygame.font.Font(None, 64)
    #text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " v: " + str(round(objekt.v[0], 2))+ " " + str(round(objekt.v[1], 2)), True, (10, 10, 10))
    text = font.render(firstinptemp, True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging"""
    pygame.display.flip()
pygame.quit()