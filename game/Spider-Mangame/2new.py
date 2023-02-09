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
# 캐릭터 이동
character_to_x = 0
#캐릭터 이동 속도
character_spped = 5

#무기 만들기
weapon = pygame.image.load("C:\\Users\\user\\Desktop\\game\\image\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapon = []

# 무기 이동 속도
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapon.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임캐릭타 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140, '''
    # 500, 200 -> 180, 160, '''
    weapon = [ [w[0], w[1] - weapon_speed] for w in weapon]
    weapon = [ [w[0], w[1]] for w in weapon if w[1] > 0]
    
    # 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapon:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapon:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종류
pygame.quit()