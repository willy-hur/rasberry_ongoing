import pygame
import time

# from TTs import*
pygame.init()  # pygame을 시작할다고 선언
interface = pygame.display.set_mode((1280, 650), 0, 32)  # 해상도 1240*720의 창을 정의


# 선택지 최대 num_size


def keyshape(counter, input_1):
    # 여기서는 키패드에서 받아온 한글, 숫자 출력문
    # 아래 4줄은 완성후 지울 예정
    if counter % 2 == 0:
        input_1 = "부산시 금정구 장전|"
    if counter % 2 == 1:
        input_1 = "엉"
    # 아래 3줄은 파이게임 창에서 택스트 출력문
    myfont = pygame.font.Font('IropkeBatangM.ttf', 35)  # 폰트 종류, 크기 설정
    message1 = myfont.render(input_1, True, (0, 0, 0))  # 출력할 텍스트, 하이라이트 색 설정
    interface.blit(message1, (465, 420))  # 출력되는 부분, 위치 설정


def edge(X_position, Y_position, X_size, Y_size):  # 사각형 선택지중 단순히 모양만 있는 부분
    color = (0, 0, 0)
    width_draw = 5
    pygame.draw.rect(interface, color, (X_position, Y_position, X_size, Y_size), width_draw)


# 열 체크하는 사진 띄우는 파트
def fever1():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/fever_check.png'), (500, 200))
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("열 채크를 시작 합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 500))


def fever2():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/001.png'), (500, 200))


def fever3():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/002.png'), (500, 200))


# 파트 1의 시작. 파일 이름은 pictures에 0폴더를 경로로
# 가장 처음 시작 선별진료소 사진을 띄워준다
def part1_show():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/001.png'), (500, 200))


# 가장처음 시작 부분에 나올 문장 출력
def intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render('안녕하세요 이길입니다. 이 기기는 시청각장애인분들의 길이 되어주기 위하여 제작하였습니다.', True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def part1_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("다음으로 넘어가려면 다음을 누르세요 만약 보지 못했을 경우 뒤로 버튼을 눌러주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (5, 540))


def part1_002():
    # 음성 추가
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
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))


# 다음을 눌러주세요 출력 2와의 차이는 위치의 차이이다
def next_2():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (800, 500))


# 예 아니요 택스트 출력 파트
def yes(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("예", True, (red, green, yellow))
    interface.blit(message1, (100, 600))


def no(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("아니요", True, (red, green, yellow))
    interface.blit(message1, (800, 600))


# 파트2의 시작 경로 위치는 picture의 1 폴더
def part2_start():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("문진표 작성을 시작합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))


# part2 사진출력
def part2_family_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/001.png'), (500, 200))


# 글씨를 화면으로 출력하는 코드
def name():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("이름을 입력해주세요.", True, (0, 0, 0))
    interface.blit(message1, (300, 100))


def sex():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("성별을 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (300, 100))


def birth():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("생년월일을 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (300, 100))


def phone_number():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("전화 번호를 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (300, 100))


def juso():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("주소를 입력해주세요", True, (0, 0, 0))
    interface.blit(message1, (300, 100))


def part2_family_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/002.png'), (200, 200))


#############################################
def part2_family_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/003.png'), (450, 200))


##############################################
def part2_family_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/004.png'), (200, 200))


def part2_family_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/005.png'), (200, 200))


def part2_family_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/006.png'), (200, 200))


# 파트2에서 symptom부분의 p_part
def check_S():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("증상 확인란 입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


# 이부분은 아래 여행력 확인 부분
def check_T():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 30)
    message1 = myfont.render("접촉 경위를 확인 합니다. 이곳을 방문하게된 이유와 맞는 것을 골라주세요", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


# 파트2에서 symptom부분의 p_part
def part2_symptom_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/001.png'), (200, 200))


def part2_symptom_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/002.png'), (100, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/003.png'), (100, 300))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/010.png'), (850, 160))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/011.png'), (850, 310))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/012.png'), (1010, 310))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/009.png'), (1010, 160))


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


# 파트2에서 travel 부분의 p_part

def part2_travel_final():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/001.png'), (200, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/002.png'), (400, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/003.png'), (600, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/004.png'), (800, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/005.png'), (200, 350))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/006.png'), (400, 350))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/007.jpg'), (600, 350))


def part2_travel_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/001.png'), (200, 200))


def part2_travel_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/002.png'), (200, 200))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/003.png'), (200, 200))


def part2_travel_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/004.png'), (200, 200))


def part2_travel_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/005.png'), (200, 200))


# 파트3 위치는 pictures부분에서 2_1폴더
def part3_start():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Medical_office_001.png'), (0, 0))


''''
def part3_1_Counseling001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Counseling/Medical_office_001.png'), (200, 200))
'''


# 코 검사
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


# 입 검사
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


# 가래
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


# 집
def part4_H_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
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


# 화장실
def part4_B_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
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
