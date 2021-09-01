import pygame
from time import sleep
from pyc import *
import time

pygame.init()


pygame.init()
interface = pygame.display.set_mode((1240, 720), 0, 32)

run = True
part: int = 0
right: int = 0
p_part: int = 0
ko: int = 0
num: int = 0
start: int = 0
enter: int = 0
fever: int = 0

def fever1():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/fever_check.png'), (500, 200))
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("열 채크를 시작 합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 600))
def fever2():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/001.png'), (500, 200))
def fever3():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/002.png'), (500, 200))

def part1_show():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/001.png'), (500, 200))


def part1_intro():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("다음으로 넘어가려면 다음을 누르세요.", True, (0, 0, 0))
    #다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (400, 100))

def part1_002():
    #음성 추가
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/002.png'), (500, 200))

def part1_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/003.png'), (500, 200))

def part1_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/004.png'), (500, 200))

def part1_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/005.png'), (500, 200))

def part1_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/006.png'), (500, 200))

def part1_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/007.png'), (500, 200))

def next():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))

def next_2():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (800, 600))
def yes():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("예", True, (0, 0, 0))
    interface.blit(message1, (100, 600))
def no():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("아니요", True, (0, 0, 0))
    interface.blit(message1, (800, 600))

def part2_start():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("문진표 작성을 시작합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))

def part2_family_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/001.png'), (500, 200))

def part2_family_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/002.png'), (200, 200))

def part2_family_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/003.png'), (200, 200))

def part2_family_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/004.png'), (200, 200))

def part2_family_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/005.png'), (200, 200))

def part2_family_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/006.png'), (200, 200))

def check():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("증상 확인란 입니다. 만약 맞는 증상이 없다면 정정을 눌러주세요", True, (0, 0, 0))
    interface.blit(message1, (10, 300))
def check_T():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("여행력을 확인 합니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))

def part2_symptom_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/001.png'), (200, 200))

def part2_symptom_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/002.png'), (200, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/003.png'), (200, 300))

def part2_symptom_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/004.png'), (200, 200))

def part2_symptom_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/005.png'), (200, 200))

def part2_symptom_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/006.png'), (200, 200))

def part2_symptom_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/007.png'), (200, 200))

def part2_symptom_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/008.png'), (200, 200))

def part2_travel_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/001.png'), (200, 200))

def part2_travel_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/002.png'), (200, 200))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/003.png'), (200, 200))

def part2_travel_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/004.png'), (200, 200))

def part2_travel_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/005.png'), (200, 200))

def part3_start():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Medical_office_001.png'), (0, 0))
''''
def part3_1_Counseling001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Counseling/Medical_office_001.png'), (200, 200))
'''

def part3_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/Medical_office_002.png'), (0, 0))
def part3_N_000():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/nose_swab_test.png'), (200, 200))
def part3_N_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N001.png'), (200, 200))
def part3_N_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N002.png'), (200, 200))
def part3_N_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N003.png'), (200, 200))
def part3_N_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N004.png'), (200, 200))

def part3_M_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/mouth_swab_test.png'), (200, 200))
def part3_M_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M001.png'), (200, 200))
def part3_M_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M002.png'), (200, 200))
def part3_M_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M003.png'), (200, 200))
def part3_M_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M004.png'), (200, 200))
def part3_M_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M005.png'), (200, 200))
def part3_M_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M006.png'), (200, 200))

#가래
def part3_P_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/phlegm_test.png'), (100, 100))
def part3_P_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P001.png'), (200, 200))
def part3_P_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P002.png'), (200, 200))
def part3_P_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P003.png'), (200, 200))
def part3_P_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P004.png'), (200, 200))
#집
def part4_H_intro():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("집에서 해야할 주의 사항입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))
def part4_H_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/001.png'), (200, 200))
def part4_H_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/002.png'), (200, 200))
def part4_H_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/003.png'), (200, 200))
def part4_H_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/004.png'), (200, 200))
def part4_H_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/005.png'), (200, 200))
def part4_H_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/006.png'), (200, 200))
def part4_H_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/007.png'), (200, 200))
def part4_H_008():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/008.png'), (200, 200))
def part4_H_009():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/009.png'), (200, 200))
def part4_H_010():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/010.png'), (200, 200))
#화장실
def part4_B_intro():
    myfont = pygame.font.Font('Maplestory Bold.ttf', 50)
    message1 = myfont.render("화장실에서 해야할 주의 사항입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))
def part4_B_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/001.png'), (200, 200))
def part4_B_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/002.png'), (200, 200))
def part4_B_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/003.png'), (200, 200))
def part4_B_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/004.png'), (200, 200))
def part4_B_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/005.png'), (200, 200))
def part4_B_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/006.png'), (200, 200))

while run:
    pygame.display.flip()
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        interface.fill((255, 255, 255))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                enter += 1
    if enter == 0 and part == 0 and p_part == 0:
        part1_show()
        part1_intro()
    if enter == 1 and part == 0 and p_part == 0:
        part = 1
    if enter == 1 and part == 1 and p_part == 0:
        part1_002()
    if enter == 2 and part == 1 and p_part == 0:
        part1_003()
    if enter == 3 and part == 1 and p_part == 0:
        part1_004()
    if enter == 4 and part == 1 and p_part == 0:
        part1_005()
    #if enter == 5 and part == 1 and p_part == 0:
        #part1_006()
    if enter == 5 and part == 1 and p_part == 0:
        part1_007()
    if enter == 6 and part == 1 and p_part == 0:
        part = 2
        enter = 0
        fever = 1
    if enter == 0 and part == 2 and p_part == 0:
        next()




    if fever == 1 and enter == 1 and part ==2 and p_part == 0:
        fever1()
    if fever == 1 and enter == 2 and part ==2 and p_part == 0:
        fever2()
    if fever == 1 and enter == 3 and part ==2 and p_part == 0:
        fever3()
    if fever == 1 and enter == 4 and part ==2 and p_part == 0:
        enter = 0
        fever = 0




    if enter == 1 and part == 2 and p_part == 0 and fever != 1:
        part2_start()
        #sleep(5)
    if enter == 2 and part == 2 and p_part == 0 and fever != 1:
        p_part = 1
    if part == 2 and enter == 2 and p_part == 1:
        part2_family_001()
    if part == 2 and enter == 3 and p_part == 1:
        part2_family_002()
        if right == 0:
            pass
            #위 아래 사진 변화 코드 필요
            #만약 아니라면
            #part2_family_003()
    if part == 2 and enter == 4 and p_part == 1:
        part2_family_004()
        # 위 아래 사진 변화 코드 필요
        # 만약 아니라면
        # part2_family_003()
    if part == 2 and enter == 5 and p_part == 1:
        part2_family_005()
        # 위 아래 사진 변화 코드 필요
        # 만약 아니라면
        # part2_family_003()
    if part == 2 and enter == 6 and p_part == 1:
        part2_family_006()
        # 위 아래 사진 변화 코드 필요
        # 만약 아니라면
        # part2_family_003()
    if part == 2 and enter == 7 and p_part == 1:
        check()
    if part == 2 and enter == 8 and p_part == 1:
        p_part = 2
        enter = 1
    if part == 2 and enter == 1 and p_part == 2:
        part2_symptom_001()
        next_2()
    if part == 2 and enter == 2 and p_part == 2:
        part2_symptom_002()

        #키패드 위아래
    if part == 2 and enter == 3 and p_part == 2:
        part2_symptom_003()
        yes()
        no()
        # if 주가 증상 + 질문
    if part == 2 and enter == 4 and p_part == 2:
        part2_symptom_004()
        yes()
        no()
        # if 주가 증상 + 질문
    if part == 2 and enter == 5 and p_part == 2:
        part2_symptom_005()
        yes()
        no()
        # if 주가 증상 + 질문
    if part == 2 and enter == 6 and p_part == 2:
        part2_symptom_006()
        yes()
        no()
        # if 주가 증상 + 질문
    if part == 2 and enter == 7 and p_part == 2:
        part2_symptom_007()
        yes()
        no()
        # if 주가 증상 + 질문
    if part == 2 and enter == 8 and p_part == 2:
        enter = 1
        p_part = 3
    if part == 2 and enter == 1 and p_part == 3:
        check_T()
    if part == 2 and enter == 2 and p_part == 3:
        part2_travel_001()
        yes()
        no()
    if part == 2 and enter == 3 and p_part == 3:
        part2_travel_002()
    if part == 2 and enter == 4 and p_part == 3:
        part2_travel_003()
        yes()
        no()
    if part == 2 and enter == 5 and p_part == 3:
        part2_travel_004()
        yes()
        no()
    if part == 2 and enter == 6 and p_part == 3:
        part = 3
        enter = 1
        p_part = 0
#상담 부분 뺼예정...

#코
    if part == 3 and enter == 1 and p_part == 0:
        part3_start()
    if part == 3 and enter == 2 and p_part == 0:
        part3_intro()
    if part == 3 and enter == 3 and p_part == 0:
        part3_N_000()
    if part == 3 and enter == 4 and p_part == 0:
        part3_N_001()
    if part == 3 and enter == 5 and p_part == 0:
        part3_N_002()
    if part == 3 and enter == 6 and p_part == 0:
        part3_N_003()
    if part == 3 and enter == 7 and p_part == 0:
        part3_N_004()
    if part == 3 and enter == 8 and p_part == 0:
        enter = 1
        p_part = 1
#입
    if part == 3 and enter == 1 and p_part == 1:
        part3_M_intro()
    if part == 3 and enter == 2 and p_part == 1:
        part3_M_001()
    if part == 3 and enter == 3 and p_part == 1:
        part3_M_002()
    if part == 3 and enter == 4 and p_part == 1:
        part3_M_003()
    if part == 3 and enter == 5 and p_part == 1:
        part3_M_004()
    if part == 3 and enter == 6 and p_part == 1:
        part3_M_005()
    if part == 3 and enter == 7 and p_part == 1:
        part3_M_006()
    if part == 3 and enter == 8 and p_part == 1:
        enter = 1
        p_part = 2
#가래
    if part == 3 and enter == 1 and p_part == 2:
        part3_P_intro()
    if part == 3 and enter == 2 and p_part == 2:
        part3_P_001()
    if part == 3 and enter == 3 and p_part == 2:
        part3_P_002()
    if part == 3 and enter == 4 and p_part == 2:
        part3_P_003()
    if part == 3 and enter == 5 and p_part == 2:
        part3_P_004()
    if part == 3 and enter == 6 and p_part == 2:
        part = 4
        enter = 1
        p_part = 0
#집
    if part == 4 and enter == 1 and p_part == 0:
        part4_H_intro()
    if part == 4 and enter == 2 and p_part == 0:
        part4_H_001()
    if part == 4 and enter == 3 and p_part == 0:
        part4_H_002()
    if part == 4 and enter == 4 and p_part == 0:
        part4_H_003()
    if part == 4 and enter == 5 and p_part == 0:
        part4_H_004()
    if part == 4 and enter == 6 and p_part == 0:
        part4_H_005()
    if part == 4 and enter == 7 and p_part == 0:
        part4_H_006()
    if part == 4 and enter == 8 and p_part == 0:
        part4_H_007()
    if part == 4 and enter == 9 and p_part == 0:
        part4_H_008()
    if part == 4 and enter == 10 and p_part == 0:
        part4_H_009()
    if part == 4 and enter == 11 and p_part == 0:
        part4_H_010()
    if part == 4 and enter == 12 and p_part == 0:
        enter = 1
        p_part = 1
    #화장실
    if part == 4 and enter == 1 and p_part == 1:
        part4_B_intro()
    if part == 4 and enter == 2 and p_part == 1:
        part4_B_001()
    if part == 4 and enter == 3 and p_part == 1:
        part4_B_002()
    if part == 4 and enter == 4 and p_part == 1:
        part4_B_003()
    if part == 4 and enter == 5 and p_part == 1:
        part4_B_004()
    if part == 4 and enter == 6 and p_part == 1:
        part4_B_005()
    if part == 4 and enter == 7 and p_part == 1:
        part4_B_006()

    pygame.display.update()

pygame.quit()
