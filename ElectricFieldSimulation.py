import SimulationCore as SimC
import pygame




pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
objekt = SimC.massObject(680, 320, 5, "blue", q = 20)
objekt2 = SimC.massObject(100, 200, 5, "red", q = 1)
objektcheck = SimC.massObject(500, 500, 5, "black", q = 1)

objlist = [objekt, objekt2]

while running:
    screen.fill("white")
    objekt.draw(screen)
    objekt2.draw(screen)
    objektcheck.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    essa = objektcheck.SimElectricField(objlist)
    objektcheck.DrawVector("E", 0.000001, screen)
    #object position debugging
    font = pygame.font.Font(None, 64)
    text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " Ex: " + str(round(objektcheck.E[0], 2)) + " Ey: "+ str(round(objektcheck.E[1], 2)), True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging
    pygame.display.flip()
pygame.quit()