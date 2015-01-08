__author__ = 'Student'
encrypt = input("Type 'enter' to start Pyong!")
if encrypt == ("enter"):
    import pygame
    import random

    pygame.init()
    bg = pygame.image.load("Images/bg.png")
    paddle1 = pygame.image.load("Images/paddle.png")
    paddle2 = pygame.image.load("Images/paddle.png")
    ball = pygame.image.load("Images/ball.png")
    windowsize = (800,600)
    screen = pygame.display.set_mode(windowsize)

    running = True
    p1MoveUp = False
    p1MoveDown = False
    p2MoveUp = False
    p2MoveDown = False
    p1YPosition = 300
    p2YPosition = 300
    clock = pygame.time.Clock()
    ballvelocity = pygame.math.Vector2(random.randint(-10,11),random.randint(-10,11))
    ballposition = (400,300)


    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    p1MoveDown = True
                if event.key == pygame.K_w:
                    p1MoveUp = True
                if event.key == pygame.K_DOWN:
                    p2MoveDown = True
                if event.key == pygame.K_UP:
                    p2MoveUp = True
                if event.key == pygame.K_r:
                    ballvelocity = pygame.math.Vector2(random.randint(-10,11),random.randint(-10,11))
                    ballposition = (400,300)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1MoveUp = False
                if event.key == pygame.K_s:
                    p1MoveDown = False
                if event.key == pygame.K_DOWN:
                    p2MoveDown = False
                if event.key == pygame.K_UP:
                    p2MoveUp = False
        screen.fill((255 ,255,255))
        if p1MoveUp:
            p1YPosition -= 5
        if p1MoveDown:
            p1YPosition += 5
        if p2MoveUp:
            p2YPosition -= 5
        if p2MoveDown:
            p2YPosition += 5
        if ballposition [1]>570:
            ballvelocity [1]*= -1
        if ballposition [1]<0:
            ballvelocity [1]*= -1
        if (0<ballposition[0]<=30) and (p1YPosition-45<ballposition[1]<=p1YPosition+45):
            ballvelocity*=-1
            ballvelocity[1] = random.randint(1, 11)
        if (750<ballposition[0]<=770) and (p2YPosition-45<ballposition[1]<=p2YPosition+45):
            ballvelocity*=-1
            ballvelocity[1] = random.randint(-11, -1)
        if ballposition [1] > p2YPosition + 10:
            p2YPosition += 10
        elif ballposition[1] < p2YPosition - 10:
            p2YPosition -= 10
        screen.blit(bg,(0,0))
        screen.blit(paddle1, (15, p1YPosition))
        screen.blit(paddle2, (770, p2YPosition))
        screen.blit(ball, ballposition)
        ballposition += ballvelocity
        pygame.display.flip()
else:
    print("Sorry invalid answer.")
