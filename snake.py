import pygame
import random
pygame.init()
font = pygame.font.Font("arial-font\\arial.ttf", 12)
class Button:
    def __init__(self, x, y, height, width, colour, border, curve, text, textColour):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border = border
        self.curve = curve
        self.text = text
        self.textColour = textColour

    def drawRect(self, event):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.colour, button, self.border, self.curve)
        if self.text != "":
            self.drawText()
        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                return True

        return False

    def drawText(self):
        text_surf = font.render(self.text, True, self.textColour)
        text_rect = text_surf.get_rect(center=(self.x+self.width//2, self.y+self.height//2))
        screen.blit(text_surf, text_rect)
def dist(p1,p2,rng):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5 < rng
def set_text(string, coordx, coordy): #Function to set text


    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
pos = [[0,10],[0,0]]
vel = [[0,1],[0,1]]
log = {}
fr = 0
appleX, appleY = random.randint(0,500),random.randint(0,500)
alive = False
speed = 0.1
rad = 25
while running:
    if alive:
        fr+=1
        delte=[]
        if(dist(pos[0],[appleX,appleY], 20)):
            speed *= 1.05
            pos.insert(0, [pos[0][0] + vel[0][0] * 10,pos[0][1] + vel[0][1] * 10])
            vel.insert(0, [vel[0][0], vel[0][1]])
            for i in log:
                log[i][1] += 1
                log[i][2] /= 1.05
            appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)
        for i in log:
            log[i][2] -=1
            if(log[i][2] <= 0):
                vel[log[i][1]] = log[i][0]
                log[i][2] = 10/speed
                log[i][1] += 1
                if(log[i][1] == len(vel)):
                    delte.append(i)
        for i in delte:
            del log[i]
        delte = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and vel[0] != [0,1]:
                    vel[0] = [0, -1]
                    log[fr] = [[0, -1], 1, 10/speed]
                elif event.key == pygame.K_d and vel[0] != [-1, 0]:
                    vel[0] = [1, 0]
                    log[fr] = [[1, 0], 1, 10/speed]
                elif event.key == pygame.K_s and vel[0] != [0,-1]:
                    vel[0] = [0, 1]
                    log[fr] = [[0, 1], 1, 10/speed]
                elif event.key == pygame.K_a and vel[0] != [1, 0]:
                    vel[0] = [-1, 0]
                    log[fr] = [[-1, 0], 1, 10/speed]
        screen.fill((0,255,0))
        for i in pos:
            pygame.draw.circle(screen, (0, 125, 0), (i[0],i[1]), 10)
            pygame.draw.circle(screen, (255, 0, 0), (appleX, appleY), 10)
            R = pygame.Rect(350, 0, 150, 25)
            pygame.draw.rect(screen, (255,255,255), R, 1)
            totalText = set_text(f"Current score: {len(pos)}", 425, 12)
            screen.blit(totalText[0], totalText[1])
        for i in range(len(vel)):
            pos[i][0] += vel[i][0] * speed
            pos[i][1] += vel[i][1] * speed
            if(pos[i][0] > 500 or pos[i][0] < 0 or pos[i][1] > 500 or pos[i][1] < 0):
                alive = False
                fr = 0
            if(dist(pos[0],pos[i],2.5) and i != 0):
                alive = False
                fr = 0
    else:

        fr += 1
        if(fr == 1):
            screen.fill((0, 255, 0))
            totalText = set_text(f"Final score: {len(pos)}", 250, 15)
            screen.blit(totalText[0], totalText[1])
        buttonEZ = Button(150, 120, 80, 200, (0, 170, 0), 0, 7, "easy", (255, 255, 255))
        buttonMed = Button(150, 210, 80, 200, (150, 150, 0), 0, 7, "medium",(255,255,255))
        buttonHard = Button(150, 300, 80, 200, (250, 150, 0), 0, 7, "hard", (255, 255, 255))
        buttonIMP = Button(150, 390, 80, 200, (170, 0, 0), 0, 7, "impossible", (255, 255, 255))
        buttonFree = Button(150, 30, 80, 200, (75, 75, 200), 0, 7, "free", (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if buttonFree.drawRect(event):
                running = True
                pos = [[0, 10], [0, 0]]
                vel = [[0, 1], [0, 1]]
                log = {}
                fr = 0
                alive = True
                rad = 50
                appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)

                speed = 0.06
            if buttonEZ.drawRect(event):
                running = True
                pos = [[0, 10], [0, 0]]
                vel = [[0, 1], [0, 1]]
                log = {}
                fr = 0
                rad = 25
                appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)
                alive = True
                speed = 0.1
            if buttonMed.drawRect(event):
                running = True
                pos = [[0, 10], [0, 0]]
                vel = [[0, 1], [0, 1]]
                log = {}
                fr = 0
                rad = 10
                appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)
                alive = True
                speed = 0.14
            if buttonHard.drawRect(event):
                running = True
                pos = [[0, 10], [0, 0]]
                vel = [[0, 1], [0, 1]]
                log = {}
                fr = 0
                rad = 0
                appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)
                alive = True
                speed = 0.2
            if buttonIMP.drawRect(event):
                running = True
                pos = [[0, 10], [0, 0]]
                vel = [[0, 1], [0, 1]]
                log = {}
                fr = 0
                rad = 0
                appleX, appleY = random.randint(rad, 500 - rad), random.randint(rad, 500 - rad)
                alive = True
                speed = 0.28
    pygame.display.flip()




# Time to end the Game
pygame.quit()
