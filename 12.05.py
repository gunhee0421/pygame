import pygame
import sys
import random

GREEN=(200,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
RED=(255,0,0)

pygame.init() 
pygame.display.set_caption("승부차기 게임")
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
img_ball=pygame.image.load("ball.png")
img_kper_M=pygame.image.load("kiper_M.png")
img_kper_L=pygame.image.load("kiper_L.png")
img_kper_R=pygame.image.load("kiper_R.png")

font=pygame.font.SysFont("malgungothic", 30)
txt1=font.render("SPACE", True, WHITE)
txt2=font.render("Start -> Enter", True, BLUE)
txt3=font.render("사용 가능한 key : A  W  D",True, BLACK)
txt4=font.render("사용 가능한 key : A Q W E D",True, BLACK)
txt13=font.render("You Loss...", True, RED)
txt14=font.render("남은 횟수 : 0회", True, WHITE)
txt15=font.render("GAME OVER...", True, RED)
txt11=font.render("Level 1 Clear!", True, RED)
txt12=font.render("Lext Level -> Enter", True, BLUE)
txt21=font.render("Level 2 CLear!!",True, RED)
txt22=font.render("Next Level -> Enter", True, BLUE)
txt23=font.render("You Loss...",True, RED)
txt24=font.render("남은 횟수 : 0회",True, WHITE)
txt25=font.render("GAME OVER...",True,RED)
txt26=font.render("Clear Level : Level 1", True, WHITE)
txt31=font.render("Level 3 Clear!!!", True, RED)
txt32=font.render("Clear Level : Level 2", True, WHITE)
txt41=font.render("GAME CLEAR!!!", True, GREEN)
txt42=font.render("축하합니다.!!!", True, WHITE)

img_goal=[
    pygame.image.load("goal.png"),
    pygame.image.load("goal2.png"),
    pygame.image.load("goal3.png"),
    pygame.image.load("goal2.png"),
    pygame.image.load("goal.png")
]
rgoal=random.randint(0,4)

img_bg10=pygame.image.load("bc.png") # 바르셀로나 경기장
img_bg11=pygame.image.load("bc1.png") # 바르셀로나 관중석   

img_bg20=pygame.image.load("bd.png") # 도르트문트 경기장
img_bg21=pygame.image.load("bd1.png") # 도르트문트 관중석

img_bg30=pygame.image.load("by.png") # 바이에른 뮌헨 경기장
img_bg31=pygame.image.load("by2.png") # 바이에른 뮌헨 관중석

img_bg40=pygame.image.load("mu.png") # 맨유 경기장
img_bg41=pygame.image.load("mu1.png") # 맨유 관중석

img_bg50=pygame.image.load("rm.png") # 레알 마드리드 경기장
img_bg51=pygame.image.load("rm1.png") # 레알 마드리드 관중석

success=0 #성공 횟수
attempt=0 #시도 횟수
anyme=0 #상대방의 성공 횟수
index=0 #게임 진행 순서
fail=0 #실패 횟수

def before_start(): 
    global index
    screen.fill(BLACK)
    screen.blit(txt1,[350,350])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if rgoal==0:
                    screen.blit(img_bg10,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_bg11,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_goal[0],[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.fill(BLACK)
                    screen.blit(txt2, [300,350])
                    pygame.display.update()
                    clock.tick(0.5)
                elif rgoal==1:
                    screen.blit(img_bg20,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_bg21,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_goal[1],[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.fill(BLACK)
                    screen.blit(txt2, [300,350])
                    pygame.display.update()
                    clock.tick(0.5)
                elif rgoal == 2:
                    screen.blit(img_bg30,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_bg31,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_goal[2],[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.fill(BLACK)
                    screen.blit(txt2, [300,350])
                    pygame.display.update()
                    clock.tick(0.5)
                elif rgoal == 3:
                    screen.blit(img_bg40,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_bg41,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_goal[1],[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.fill(BLACK)
                    screen.blit(txt2, [300,350])
                    pygame.display.update()
                    clock.tick(0.5)
                elif rgoal == 4: 
                    screen.blit(img_bg50,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_bg51,[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.blit(img_goal[0],[0, 100])
                    pygame.display.update()
                    clock.tick(0.5)
                    screen.fill(BLACK)
                    screen.blit(txt2, [300,350])
                    pygame.display.update()
                    clock.tick(0.5)

def made_kiper_1():
    screen.fill(GREEN)
    screen.blit(img_goal[rgoal], [0,100])
    txt_success=font.render("success: "+str(success), True, BLUE)
    screen.blit(txt_success,[300,10])
    txt_fail=font.render("anyme: "+str(anyme), True, RED)
    screen.blit(txt_fail,[650,10])
    txt_attempt=font.render("attempt: "+str((attempt)%5), True, BLACK)
    screen.blit(txt_attempt,[10,10])
    screen.blit(txt3,[200, 720])
    pygame.display.update()

def made_kiper_2():
    screen.fill(GREEN)
    screen.blit(img_goal[rgoal], [0,100])
    txt_success=font.render("success: "+str(success), True, BLUE)
    screen.blit(txt_success,[300,10])
    txt_fail=font.render("anyme: "+str(anyme), True, RED)
    screen.blit(txt_fail,[650,10])
    txt_attempt=font.render("attempt: "+str((attempt)%5), True, BLACK)
    screen.blit(txt_attempt,[10,10])
    screen.blit(txt4,[200,720])
    pygame.display.update()

def madescreen_1():
    screen.fill(GREEN)
    screen.blit(img_goal[rgoal], [0,100])
    screen.blit(img_ball,[375,600])
    screen.blit(img_kper_M, [350,250])
    txt_success=font.render("success: "+str(success), True, BLUE)
    screen.blit(txt_success,[300,10])
    txt_fail=font.render("anyme: "+str(anyme), True, RED)
    screen.blit(txt_fail,[650,10])
    txt_attempt=font.render("attempt: "+str((attempt)%5), True, BLACK)
    screen.blit(txt_attempt,[10,10])
    screen.blit(txt3,[200, 720])
    pygame.display.update()

def madescreen_2():
    screen.fill(GREEN)
    screen.blit(img_goal[rgoal], [0,100])
    screen.blit(img_ball,[375,600])
    screen.blit(img_kper_M, [350,250])
    txt_success=font.render("success: "+str(success), True, BLUE)
    screen.blit(txt_success,[300,10])
    txt_fail=font.render("anyme: "+str(anyme), True, RED)
    screen.blit(txt_fail,[650,10])
    txt_attempt=font.render("attempt: "+str((attempt)%5), True, BLACK)
    screen.blit(txt_attempt,[10,10])
    screen.blit(txt4,[200,720])
    pygame.display.update()


def level_1(): 
    for event in pygame.event.get():
        global success
        global fail
        global attempt
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                com=random.randint(1,3)
                made_kiper_1()
                if com==1:
                    screen.blit(img_kper_L,[100, 200])
                    screen.blit(img_ball,[150, 250])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[150, 250])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 200])
                    screen.blit(img_ball,[150, 250])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_w:
                com=random.randint(1,3)
                made_kiper_1()
                if com==1:
                    screen.blit(img_kper_L,[100, 200])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 200])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_d: 
                com=random.randint(1,3)
                made_kiper_1()
                if com==1:
                    screen.blit(img_kper_L,[100, 200])
                    screen.blit(img_ball,[550, 250])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[550, 230])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 200])
                    screen.blit(img_ball,[550, 250])
                    pygame.display.update()
                    attempt=attempt+1
        clock.tick(4)
def level_2():  
    for event in pygame.event.get():
        global success
        global fail
        global attempt
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                com=random.randint(1,5)
                made_kiper_2()
                if com==1:
                    screen.blit(img_kper_L,[100, 300])
                    screen.blit(img_ball,[150, 350])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[150, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 300])
                    screen.blit(img_ball,[150, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==4:
                    screen.blit(img_kper_L,[100, 180])
                    screen.blit(img_ball,[150, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==5:
                    screen.blit(img_kper_R,[500, 180])
                    screen.blit(img_ball,[150, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_w:
                com=random.randint(1,5)
                made_kiper_2()
                if com==1:
                    screen.blit(img_kper_L,[100, 300])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 300])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==4:
                    screen.blit(img_kper_L,[100, 180])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==5:
                    screen.blit(img_kper_R,[500, 180])
                    screen.blit(img_ball,[350, 210])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_d:
                com=random.randint(1,5)
                made_kiper_2()
                if com==1:
                    screen.blit(img_kper_L,[100, 300])
                    screen.blit(img_ball,[600, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[600, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 300])
                    screen.blit(img_ball,[600, 350])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==4:
                    screen.blit(img_kper_L,[100, 180])
                    screen.blit(img_ball,[600, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==5:
                    screen.blit(img_kper_R,[500, 180])
                    screen.blit(img_ball,[600, 350])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_q:
                com=random.randint(1,5)
                made_kiper_2()
                if com==1:
                    screen.blit(img_kper_L,[100, 300])
                    screen.blit(img_ball,[150, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[150, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 300])
                    screen.blit(img_ball,[150, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==4:
                    screen.blit(img_kper_L,[100, 180])
                    screen.blit(img_ball,[150, 200])
                    pygame.display.update()
                    attempt=attempt+1
                elif com==5:
                    screen.blit(img_kper_R,[500, 180])
                    screen.blit(img_ball,[150, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
            if event.key==pygame.K_e:
                com=random.randint(1,5)
                made_kiper_2()
                if com==1:
                    screen.blit(img_kper_L,[100, 300])
                    screen.blit(img_ball,[600, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==2:
                    screen.blit(img_kper_M,[350, 180])
                    screen.blit(img_ball,[600, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==3:
                    screen.blit(img_kper_R,[500, 300])
                    screen.blit(img_ball,[600, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==4:
                    screen.blit(img_kper_L,[100, 180])
                    screen.blit(img_ball,[600, 200])
                    pygame.display.update()
                    success=success+1
                    attempt=attempt+1
                elif com==5:
                    screen.blit(img_kper_R,[500, 180])
                    screen.blit(img_ball,[600, 200])
                    pygame.display.update()
                    attempt=attempt+1
        clock.tick(4)

def level_3(): 
    for event in pygame.event.get():
        global success
        global attempt
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                com_2=random.randint(1,2)
                com_move=random.randint(1,5)
                made_kiper_2()
                if com_move==1:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [150, 350])
                        pygame.display.update()
                        attempt=attempt+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [10, 350])
                        pygame.display.update()
                        attempt=attempt+1
                elif com_move==2:
                    if com_2==1:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [150, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [10, 350])
                        pygame.display.update()
                        attempt=attempt+1
                elif com_move==3:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [150, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [10, 350])
                        pygame.display.update()
                        attempt=attempt+1
                elif com_move==4:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [150, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [10, 350])
                        pygame.display.update()
                        attempt=attempt+1
                elif com_move==5:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [150, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [10, 350])
                        pygame.display.update()
                        attempt=attempt+1
            if event.key==pygame.K_w:
                com_2=random.randint(1,2)
                com_move=random.randint(1,5)
                made_kiper_2()
                if com_move==1:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [350, 210])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [350, 110])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==2:
                    if com_2==1:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [350, 210])
                        pygame.display.update()
                        attempt=attempt+1
                    elif com_2==2:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [350, 110])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==3:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [350, 210])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [350, 110])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==4:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [350, 210])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [350, 110])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==5:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [350, 210])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [350, 110])
                        pygame.display.update()
                        attempt=attempt+1
            if event.key==pygame.K_d:
                com_2=random.randint(1,2)
                com_move=random.randint(1,5)
                made_kiper_2()
                if com_move==1:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [600, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [750, 350])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==2:
                    if com_2==1:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [600, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [750, 350])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==3:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [600, 350])
                        pygame.display.update()
                        attempt=attempt+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [750, 350])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==4:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [600, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [750, 350])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==5:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [600, 350])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [750, 350])
                        pygame.display.update()
                        attempt=attempt+1
            if event.key==pygame.K_q:
                com_2=random.randint(1,2)
                com_move=random.randint(1,5)
                made_kiper_2()
                if com_move==1:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [100, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [50, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==2:
                    if com_2==1:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [100, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [50, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==3:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [100, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [50, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==4:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [100, 200])
                        pygame.display.update()
                        attempt=attempt+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [50, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==5:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [100, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [50, 130])
                        pygame.display.update()
                        attempt=attempt+1
            if event.key==pygame.K_e:
                com_2=random.randint(1,2)
                com_move=random.randint(1,5)
                made_kiper_2()
                if com_move==1:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [600, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 300])
                        screen.blit(img_ball, [750, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==2:
                    if com_2==1:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [600, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_M, [350, 180])
                        screen.blit(img_ball, [750, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==3:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [600, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 300])
                        screen.blit(img_ball, [750, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==4:
                    if com_2==1:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [600, 200])
                        pygame.display.update()
                        attempt=attempt+1
                        success=success+1
                    elif com_2==2:
                        screen.blit(img_kper_L, [100, 180])
                        screen.blit(img_ball, [750, 130])
                        pygame.display.update()
                        attempt=attempt+1
                if com_move==5:
                    if com_2==1:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [600, 200])
                        pygame.display.update()
                        attempt=attempt+1
                    elif com_2==2:
                        screen.blit(img_kper_R, [500, 180])
                        screen.blit(img_ball, [750, 130])
                        pygame.display.update()
                        attempt=attempt+1
        clock.tick(4)

def reset():
    global success, anyme, attempt
    success=0
    anyme=0
    attempt=0

def anyme_success():
    global anyme
    anyme=random.randint(1,100)
    if anyme==0:
        anyme=0
    elif anyme>0 and anyme<30:
        anyme=1
    elif anyme>30 and anyme<61:
        anyme=2
    elif anyme>61 and anyme<81:
        anyme=3
    elif anyme>81 and anyme<91:
        anyme=4
    else:
        anyme=5

def main():
    global attempt, index, fail
    index=0
    fail=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        if index==0: #배경 선택
            before_start()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        index=1
        if index==1: #1단계 진행
            anyme_success()
            while(attempt<=5):
                madescreen_1()
                level_1()
                if attempt<=5:
                    if success>anyme:
                        screen.fill(BLACK)
                        screen.blit(txt11, [300, 325])
                        screen.blit(txt12, [275, 400])
                        pygame.display.update()
                        clock.tick(0.25)
                        attempt=10
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_RETURN:
                                    index=2
                    if attempt==5 and success<=anyme:
                        if fail==0:
                            screen.fill(BLACK)
                            screen.blit(txt13, [300, 325])
                            screen.blit(txt14,[270,400])
                            pygame.display.update()
                            clock.tick(0.5)
                            reset()
                            anyme_success()
                            index=1
                            fail=1
                        else:
                            screen.fill(BLACK)
                            screen.blit(txt15,[300,325])
                            pygame.display.update()
                            clock.tick(0.5)
                            pygame.quit()

        elif index==2: #2단계 진행
            fail=0
            reset()
            anyme_success()
            while(attempt<=5):
                madescreen_2()
                level_2()
                if attempt<=5:
                    if success>anyme:
                        screen.fill(BLACK)
                        screen.blit(txt21, [300, 325])
                        screen.blit(txt22, [275, 400])
                        pygame.display.update()
                        clock.tick(0.25)
                        attempt=10
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_RETURN:
                                    index=3
                    elif attempt==5 and success<=anyme:
                        if fail==0:
                            screen.fill(BLACK)
                            screen.blit(txt23, [300, 325])
                            screen.blit(txt24,[270,400])
                            pygame.display.update()
                            clock.tick(0.5)
                            reset()
                            anyme_success()
                            index=2
                            fail=1
                        else:
                            screen.fill(BLACK)
                            screen.blit(txt26,[275,325])
                            screen.blit(txt25, [300,400])
                            pygame.display.update()
                            clock.tick(0.5)
                            pygame.quit()
        elif index==3: #3단계 진행
            fail=0
            reset()
            anyme_success()
            while(attempt<=5):
                madescreen_2()
                level_3()
                if attempt<=5:
                    if success>anyme:
                        screen.fill(BLACK)
                        screen.blit(txt31, [300, 325])
                        pygame.display.update()
                        clock.tick(0.25)
                        attempt=10
                    elif attempt==5 and success<=anyme:
                        if fail==0:
                            screen.fill(BLACK)
                            screen.blit(txt23, [300, 325])
                            screen.blit(txt24,[270,400])
                            pygame.display.update()
                            clock.tick(0.5)
                            reset()
                            anyme_success()
                            index=3
                            fail=1
                        else:
                            screen.fill(BLACK)
                            screen.blit(txt32,[275,325])
                            screen.blit(txt25, [300,400])
                            pygame.display.update()
                            clock.tick(0.5)
                            pygame.quit()
            if attempt==10:
                index=4
        elif index==4: #경기 종료
            screen.fill(BLACK)
            screen.blit(txt41,[300,325])
            screen.blit(txt42,[315,400])
            pygame.display.update()
            clock.tick(0.25)
            exit()

main()