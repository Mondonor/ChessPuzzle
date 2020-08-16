#libraries
import pygame
from pygame.locals import *

import random
from random import seed
from random import randint

import math

from itertools import combinations

def variableReset():
    global n, W, H, font, font2, win, bits, bitList, SquareList, white, red, yellow, blue
    n = int(input("What size square board would you like?"))

    W = 1200
    H = 1000

    font = pygame.font.Font('freesansbold.ttf', 20)
    font2 = pygame.font.Font('freesansbold.ttf', 12)

    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Puzlle :)")

    IntroScreen()
    
    bits = math.ceil(math.log(n**2, 2))

    bitList = [[]] * bits

    white  = (255, 255, 255)
    red    = (255, 0, 0)
    yellow = (255, 255, 0)
    blue   = (0, 0, 255)

def IntroScreen():
    textIntro = font2.render("'a' to assign/reassign all properties, press 'd' to draw the board, press q to quit", True, (0,255,255))
    textIntroRect = textIntro.get_rect()
    textIntroRect.center = (int(H/2), int(W/2))
    win.fill((0,0,0))
    win.blit(textIntro, textIntroRect)
    pygame.display.update()
    

    
    
    

def draw():
    win.fill((0,0,0))
    global squareList, bitList
    #draw the board
    for i in range(n):
        for j in range(n):
            if i%2 == 0 and j%2 == 0:
                pygame.draw.rect(win, (255,255,255), (int(squareList[(n*i) + j][0]), int(squareList[(n*i) + j][1]),int(Pwidth),int(Pheight)))
            elif i%2 == 0 and j%2 == 1:
               pygame.draw.rect(win, (0,0,0), (int(squareList[(n*i) + j][0]), int(squareList[(n*i) + j][1]),int(Pwidth),int(Pheight)))
            elif i%2 == 1 and j%2 == 0:
                pygame.draw.rect(win, (0,0,0), (int(squareList[(n*i) + j][0]), int(squareList[(n*i) + j][1]),int(Pwidth),int(Pheight)))
            else:
                pygame.draw.rect(win, (255,255,255), (int(squareList[(n*i) + j][0]), int(squareList[(n*i) + j][1]),int(Pwidth),int(Pheight)))
            #draw the circles
            if squareList[(n*i)+j][2] == 1:
                pygame.draw.circle(win, blue, [(int(squareList[(n*i) + j][0])) + int(Pwidth / 2),(int(squareList[(n*i) + j][1])) + int(Pwidth / 2)], int(Pwidth/2.5))
            else:
                pygame.draw.circle(win, red, [(int(squareList[(n*i) + j][0])) + int(Pwidth / 2),(int(squareList[(n*i) + j][1])) + int(Pwidth / 2)], int(Pwidth/2.5))
    #draw the bits / bits-square
    for k in range(bits):
        pygame.draw.rect(win, (255,255,255), (int(bitList[k][0]), int(bitList[k][1]),int(W /(2*bits)),int(W /(2*bits))))
        text = font.render(f"{int((bitList[bits - 1 - k][2]+1)/2)}", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (int(bitList[k][0]+ int(W / (4*bits))), int(bitList[k][1] + int(W /(4*bits))))
        win.blit(text, textRect)

    #draw the key
    pygame.draw.rect(win, yellow, (int(squareList[keyPOS][0]), int(squareList[keyPOS][1]),int(Pwidth/4),int(Pwidth/4)))

    #drawTest
    if possibilityCondition == False:
        text1 = font2.render("I'm sorry, there is no possible ", True, (0,255,255))
        text2 = font2.render("button-mapping for this size board.", True, (0, 255, 255))
        text3 = font2.render("This is due to there not being" , True, (0,255,255))
        text4 = font2.render("enough squares required to affect all combinations of bits.", True, (0, 255, 255))
        text1Rect = text1.get_rect()
        text2Rect = text2.get_rect()
        text3Rect = text3.get_rect()
        text4Rect = text4.get_rect()
        text1Rect.center = (int(.82*W), int(4*H/14))
        text2Rect.center = (int(.82*W), int(5*H/14))
        text3Rect.center = (int(.82*W), int(6*H/14))
        text4Rect.center = (int(.82*W), int(7*H/14))
        win.blit(text1,text1Rect)
        win.blit(text2,text2Rect)
        win.blit(text3,text3Rect)
        win.blit(text4,text4Rect)

    if solBool:
        textKey = font2.render(f"Actual Key Position is: {keyBits}", True, (0, 255, 255))
        textKEYRect = textKey.get_rect()
        textKEYRect.center = (int(W/2) , int(.85 * H))
        win.blit(textKey, textKEYRect)
    
    text5 = font2.render(f"There is {LHsum} required squares to be able ", True, (0,255,255))
    text6 = font2.render(f" to perform a proper map, {n**2} squares are needed.", True, (0, 255, 255))
    text7 = font2.render("See Documentation for more details.", True, (0, 255, 255))
    
    text5Rect = text5.get_rect()
    text6Rect = text6.get_rect()
    text7Rect = text7.get_rect()
    
    text5Rect.center = (int(.82*W), int(8*H/14))
    text6Rect.center = (int(.82*W), int(9*H/14))
    text7Rect.center = (int(.82*W), int(10*H/14))
    
    win.blit(text5,text5Rect)
    win.blit(text6,text6Rect)
    win.blit(text7,text7Rect)
    print(bitList)



def assign():
    #Creates information about bitList, squareList, key pos,
    #randomly generates heads or tails, and defines connection between buttons and bits
    global n, H, W, squareList, Pwidth, Pheight, keyPOS, lis, finlis, possibilityCondition, LHsum, keyBin
    BoardHeight = H * .8
    BoardWidth = H * .8
    Pwidth = BoardWidth / n
    Pheight = Pwidth
    squareList = [[]] * (n**2)

    for i in range(n**2):
        squareList[i] = [int(int(Pwidth * (i%n))), int(int(i / n) * Pheight), (random.randint(0,1)*2)-1]
    for i in range(bits):
        bitList[i] = [(((bits - 1 - i) / bits)/1.5) * W, .9*H,1]

    keyPOS = random.randint(0, (n**2)-1)

    keyBits = []

    #beginning of alg
    LHsum = 0
    for m in range(bits+1):
        LHsum = LHsum + math.comb(bits, m)
    if LHsum <= n**2:
        possibilityCondition = True
    else: possibilityCondition = False

    if possibilityCondition:
        lis = []
        finlis = []

        for i in range(bits):
            lis.append(i)

        for i in range(bits):
            for j in range(len(list(combinations(lis, i)))):
                finlis.append(list(combinations(lis,i))[j])
        finlis.append(tuple(lis))


        
        #ASSIGN TUPLES INTO SQUARELIST IN INDEX 3
        for j in range(len(squareList)):
            squareList[j].append(finlis[j])

        for j in range(len(squareList)):
            for k in range(bits):
                if k in squareList[j][3]:
                    bitList[k][2] = bitList[k][2] * squareList[j][2]
        
    solBool = False


def Solution():
    # Which Square Will change the bits?
    # Find which bits I need to change
    global fixerList, keyBits, keyBitstemp, indexor, solBool

    #Find the binary version of keyPOS
    keyPOS2 = keyPOS
    keyBitstemp = []
    for i in range(bits):
        keyBitstemp.append(keyPOS2%2)
        keyPOS2 = int(keyPOS2 / 2)
    keyBitstemp.reverse()
    keyBits = keyBitstemp


    fixerList = []
    
    for x in range(bits):
        if (bitList[x][2]+1)/2 != keyBits[x]:
            fixerList.append(x)

    print(bitList)
    print(fixerList)
    print(keyBits)
    indexor = 0

    for y in range(len(squareList)):
        if squareList[y][3] == tuple(fixerList):
            indexor = y
        elif len(fixerList) == 1:
            if len(squareList[y][3]) == 0:
                continue
            if squareList[y][3][0] == fixerList[0]:
                indexor = y

    squareList[indexor][2] = squareList[indexor][2] * (-1)
   
    
    print(f"YOU MUST FLIP THE {indexor+1}'th BUTTON!!!")
    
    for o in range(bits):
        bitList[o][2] = 1
    
    for j in range(len(squareList)):
        for k in range(bits):
            if k in squareList[j][3]:
                bitList[k][2] = bitList[k][2] * squareList[j][2]


    solBool = True
    



def main():
    global solBool
    solBool = False
    pygame.init()
    variableReset()
    r = True
    while r:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                r = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_q:
                    r = False
                elif event.key == pygame.K_r:
                    variableReset()
                elif event.key == pygame.K_a:
                    assign()
                    draw()
                elif event.key == pygame.K_d:
                    draw()
                elif event.key == pygame.K_s:
                    Solution()
                    pygame.time.delay(2000)
                    draw()

        pygame.display.update()
    pygame.quit()
    
main()
