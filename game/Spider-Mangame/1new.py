from numpy import character
import pygame

pygame.init()

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("gosu Game")

# fps
clock = pygame.time.Clock()

##########################################
# 배경 만들기
background = pygame.image.load("C:\\Users\\user\\Desktop\\game\\image\\back.png")
# 스테이지
stage = pygame.image.load("C:\\Users\\user\\Desktop\\game\\image\\back(1).png")
stage_size = stage.get_rect().size
stage_height = stage_size[1]
# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\user\\Desktop\\game\\image\\cha.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    df = clock.tick(30)

# 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종류
pygame.quit()