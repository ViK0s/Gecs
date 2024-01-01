import SimulationCore as SimC
import pygame
import sys

inputvar = sys.argv

#this should be in interface core, only for the interactive mode, but I didn't have time to implement
print("Input x of test charge")
tempinputx = input()
print("Input y of test charge")
tempinputy = input()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
test_charge = SimC.massObject(int(tempinputx), int(tempinputy), 5, "black", q = 1)

def drawgroup(objlist):
    for i in objlist:
        i.draw(screen)
        #calling value from object into object method seems bad
        i.DrawValue(i.q, screen)

def ChangeColor(objlist):
    for i in objlist:
        if i.q > 0:
            i.color = "red"
        else:
            i.color = "blue"

#this is kinda unreadable?

x = SimC.ObjSpawn(SimC.afterConvert(SimC.SplitStringIntoList(inputvar[1])), int(inputvar[6]), 0, 0, SimC.SplitStringIntoList(inputvar[5]), 0)
ChangeColor(x)

while running:
    screen.fill("white")
    test_charge.draw(screen)
    drawgroup(x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    test_charge.SimElectricField(x)
    test_charge.DrawVector("E", 0.000001, screen)
    pygame.display.flip()
pygame.quit()