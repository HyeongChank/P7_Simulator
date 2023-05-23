import pygame
import sys

# 초기 설정
pygame.init()
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

# 트럭 설정
truck_width, truck_height = 80, 50
truck_x, truck_y = win_width // 2, win_height - truck_height - 20
truck_speed = 2

# 메인 루프
running = True
while running:
    pygame.time.delay(10)  # 프레임 속도 조절

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 종료 이벤트
            running = False

    # 트럭 움직임
    keys = pygame.key.get_pressed()  # 눌린 키 확인
    if keys[pygame.K_LEFT] and truck_x - truck_speed > 0:  # 왼쪽 키가 눌리면, 왼쪽으로 이동
        truck_x -= truck_speed
    if keys[pygame.K_RIGHT] and truck_x + truck_speed < win_width - truck_width:  # 오른쪽 키가 눌리면, 오른쪽으로 이동
        truck_x += truck_speed

    # 화면 그리기
    win.fill((255, 255, 255))  # 배경색 지우기
    pygame.draw.rect(win, (0, 0, 255), pygame.Rect(truck_x, truck_y, truck_width, truck_height))  # 트럭 그리기
    pygame.display.update()  # 화면 업데이트

pygame.quit()
sys.exit()
