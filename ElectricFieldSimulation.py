import SimulationCore as SimC
import pygame
import sys

input = sys.argv


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
#better var name needed, this object is supposed to be the "test charge"
test_charge = SimC.massObject(500, 500, 5, "black", q = 1)
def drawgroup(objlist):
    for i in objlist:
        i.draw(screen)

def ChangeColor(objlist):
    for i in objlist:
        if i.q > 0:
            i.color = "red"
        else:
            i.color = "blue"

#this is kinda unreadable?
#print(SimC.SplitStringIntoList(input[1]))

x = SimC.ObjSpawn(SimC.afterConvert(SimC.SplitStringIntoList(input[1])), int(input[6]), 0, 0, SimC.SplitStringIntoList(input[5]), 0)
ChangeColor(x)
print(SimC.SplitStringIntoList(input[5]))
while running:
    screen.fill("white")
    test_charge.draw(screen)
    drawgroup(x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    test_charge.SimElectricField(x)
    test_charge.DrawVector("E", 0.000001, screen)
    #object position debugging
    """font = pygame.font.Font(None, 64)
    text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " Ex: " + str(round(objektcheck.E[0], 2)) + " Ey: "+ str(round(objektcheck.E[1], 2)), True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging"""
    pygame.display.flip()
pygame.quit()