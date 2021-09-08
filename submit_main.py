from submit_main_def import*
import csv
pygame.init()

run = True
part: int = 0
right: int = 0
p_part: int = 0
ko: int = 0
num: int = 0
start: int = 0
enter: int = 0
fever: int = 0
input_t: int = 0
first = 0
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
            elif event.key == pygame.K_RETURN:
                enter -= 1


    if enter == 0 and part == 0 and p_part == 0:
        part1_show()
        part1_intro()
        first_time()

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
    #clock.tick(30)
pygame.quit()
