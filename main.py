import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((612, 367)) # flags=pygame.NOFRAME
pygame.display.set_caption("Pygame Daulet")
icon = pygame.image.load('images/ic.png').convert_alpha()
pygame.display.set_icon(icon)

#Player
bg = pygame.image.load('images/bg.jpg').convert()
walk_left = [
    pygame.image.load('images/player_left/player_left1.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left2.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left3.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left4.png').convert_alpha()
]
walk_right = [
    pygame.image.load('images/player_right/player_rigth1.png').convert_alpha(),
    pygame.image.load('images/player_right/player_rigth2.png').convert_alpha(),
    pygame.image.load('images/player_right/player_rigth3.png').convert_alpha(),
    pygame.image.load('images/player_right/player_rigth4.png').convert_alpha()
]



ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_list_in_game = []



player_anim_count = 0

player_speed = 5
player_x = 150
player_y = 250
is_jump = False
jump_count = 8

bg_x = 0
bg_sound = pygame.mixer.Sound('music/bg_music.mp3')
bg_sound.play()


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('fonts/KZ_SamsungSharpSans.ttf', 40)
lose_label = label.render('Сіз жеңілдіңіз!', True, (193, 196, 199))
restart_label = label.render('Қайтадан ойнау', True, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(140, 220))

gameplay = True


running = True
while running:


    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 612, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))


        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))


        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -612:
            bg_x = 0
    else:
        bg_sound.stop()
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (150, 120))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()


    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(614, 250)))

    clock.tick(10)
