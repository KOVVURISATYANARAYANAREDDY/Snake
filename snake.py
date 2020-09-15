import pygame
from pygame import display, event, image, font
import random
import time
pygame.init()

screen = display.set_mode((800,850))
display.set_caption('Snake Game')
score = 0
font1 = font.Font('freesansbold.ttf',28)
left = False
right = False
up = False
down = False

block_x = (random.randint(10,785) // 10)*10
block_y = (random.randint(10,785) // 10)*10

l = [[300, 300]]

Running = True
while Running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 225, 0), (block_x, block_y, 10, 10))
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            Running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                if right != True:
                    left = True
                    right = False
                    up = False
                    down = False
            if e.key == pygame.K_LEFT:
                if left != True:
                    left = False
                    right = True
                    up = False
                    down = False
            if e.key == pygame.K_UP:
                if down != True:
                    left = False
                    right = False
                    up = True
                    down = False
            if e.key == pygame.K_DOWN:
                if up != True:
                    left = False
                    right = False
                    up = False
                    down = True

    a = l[0].copy()
    b = l[0].copy()
    l = l[0:-1]
    if left == True:
        if a[0]<790:
            a[0] += 10
        else:
            break
    elif right == True:
        if a[0] > 10:
            a[0] -= 10
        else:
            break
    elif up == True:
        if a[1] > 10:
            a[1] -= 10
        else:
            break
    elif down == True:
        if a[1] < 790:
            a[1] += 10
        else:
            break
    if a not in l:
        l.insert(0,a)
    else:
        l.insert(0,b)
        break
        
    
    time.sleep(0.05)
    if l[0][0] == block_x and l[0][1] == block_y:
        block_x = (random.randint(10,785) // 10)*10
        block_y = (random.randint(10,785) // 10)*10
        a = l[-1].copy()
        score += 1
        a[0] += 10
        l.append(a)
    for i in range(0,len(l)):
        x,y = l[i][0], l[i][1]
        pygame.draw.rect(screen, (0, 225, 255), (x, y, 8, 8))
    label = 'Score: ' + str(score)
    text = font1.render(label,True,(0, 255, 0))
    pygame.draw.rect(screen, (0, 225, 255), (0, 800, 800, 4))
    screen.blit(text, (10, 810))
    display.update()
            
print('Score :', score)
