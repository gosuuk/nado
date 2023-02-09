import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("gosu Game")

# 배경이미지 불러오기

background = pygame.image.load("C:/Users/user/Desktop/game/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/user/Desktop/game/chart.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당한느 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False


      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              to_x -= 5
          elif event.key == pygame.K_RIGHT:
              to_x += 5
          elif event.key == pygame.K_UP:
              to_y -= 5
          elif event.key == pygame.K_DOWN:
              to_y += 5

      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              to_x = 0
          elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
              to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height 


    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기
    
# pygame 종류
pygame.quit()