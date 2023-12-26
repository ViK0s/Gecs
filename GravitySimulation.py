import SimulationCore as SimC
import pygame




pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
objekt = SimC.massObject(680, 320, 5, "blue", 20000000000000, [0,0])
objekt2 = SimC.massObject(100, 200, 5, "red", 1000000000000,[1,-1])
dt = 0


while running:
    screen.fill("white")
    objekt.draw(screen)
    objekt2.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    objekt.SimulateGravity(objekt2, dt)
    objekt2.SimulateGravity(objekt, dt)
    objekt.DrawVector("v", 100, screen)
    #object position debugging
    font = pygame.font.Font(None, 64)
    text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " v: " + str(round(objekt.v[0], 2))+ " " + str(round(objekt.v[1], 2)), True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()