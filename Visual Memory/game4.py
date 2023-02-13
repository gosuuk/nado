import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1 
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 grid cell
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_bottons.append(button)

    print(grid)


# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button

def display_game_screen():
    for idx, rect in enumerate(number_bottons, start=1):
        pygame.draw.rect(screen, GRAY, rect)

        # 실제 숫자 텍스트
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text, text_rect)

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
  global start
  if start_button.collidepoint(pos):
        start = True
# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("gosu game")
game_font = pygame.font.Font(None, 120) # 폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)


number_bottons = []
# 게임 시작 여부
start = False

setup(1)

#게임 루프
running = True # 게임이 실행중
while running:
    click_pos = None
    
    # 이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실해중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 화면 전체를 까망게
    screen.fill(BLACK)

    if start: # 게임 화면 표시
        display_game_screen()
    else:
        display_start_screen()
    
    # 사용자가 클릭한 좌표값
    if click_pos:
        check_buttons(click_pos)

    #화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()