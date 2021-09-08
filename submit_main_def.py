import pygame
pygame.init()
interface = pygame.display.set_mode((1240, 720), 0, 32)
def first_time():
    pass

def edge():
    color = (0,0,0)
    width_draw = 5
    pygame.draw.rect(interface, color, (20, 100, 50, 50), width_draw)

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
    myfont = pygame.font.Font('Maplestory Bold.ttf', 40)
    message1 = myfont.render("다음으로 넘어가려면 다음을 누르세요 만약 보지 못했을 경우 정정을 눌러주세요.", True, (0, 0, 0))
    #다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (0, 100))


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
